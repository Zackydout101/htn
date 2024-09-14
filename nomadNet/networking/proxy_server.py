
from aiohttp import web
from utils.logging import logger
from core.auth import authenticate, auth_middleware

class ProxyServer:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.app = web.Application(middlewares=[auth_middleware])
        self.app.router.add_post('/proxy', self.handle_proxy_request)
        self.app.router.add_get('/get_proxy', self.get_proxy)

    async def start(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8080)
        await site.start()
        logger.info("Proxy server started on http://0.0.0.0:8080")

    async def handle_proxy_request(self, request):
        request_data = await request.json()
        response = await self.proxy_manager.handle_request(request_data)
        return web.json_response(response)

    async def get_proxy(self, request):
        domain = request.query.get('domain')
        if not domain:
            return web.json_response({'error': 'Domain parameter is required'}, status=400)
        
        modem = await self.proxy_manager.get_proxy(domain)
        return web.json_response({'proxy_id': modem.id})