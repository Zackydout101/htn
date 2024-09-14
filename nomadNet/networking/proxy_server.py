import asyncio
from aiohttp import web
import aiohttp
from urllib.parse import urlparse
from core.auth import validate_token
from utils.logging import logger

class ProxyServer:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.app = web.Application()
        self.app.router.add_route('*', '/{path:.*}', self.handle_request)

    async def handle_request(self, request):
        if request.method == 'CONNECT':
            return await self.handle_connect(request)
        else:
            return await self.handle_http(request)

    async def handle_connect(self, request):
        host, port = request.path.split(':')
        modem = await self.proxy_manager.get_proxy(host)

        reader, writer = await asyncio.open_connection(host, int(port), local_addr=(modem.ip_address, 0))
        
        await request.writer.write(b'HTTP/1.1 200 Connection established\r\n\r\n')
        
        async def pipe(reader, writer):
            try:
                while True:
                    data = await reader.read(8192)
                    if not data:
                        break
                    writer.write(data)
                    await writer.drain()
            finally:
                writer.close()
        
        await asyncio.gather(
            pipe(request.transport, writer),
            pipe(reader, request.transport)
        )
        
        return web.Response()

    async def handle_http(self, request):
        url = str(request.url)
        parsed_url = urlparse(url)
        modem = await self.proxy_manager.get_proxy(parsed_url.netloc)

        headers = dict(request.headers)
        headers.pop('Host', None)

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method=request.method,
                url=url,
                headers=headers,
                data=await request.read(),
                ssl=False,
                proxy=f"http://{modem.ip_address}:0"
            ) as response:
                body = await response.read()
                return web.Response(
                    body=body,
                    status=response.status,
                    headers=response.headers
                )

    async def start(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8080)
        await site.start()
        logger.info("Proxy server started on http://0.0.0.0:8080")