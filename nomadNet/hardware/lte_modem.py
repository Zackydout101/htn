import asyncio
import aiohttp
from utils.logging import logger

class LTEModem:
    def __init__(self, id, device):
        self.id = id
        self.device = device
        self.session = None

    async def connect(self):
        # Simulate modem connection
        await asyncio.sleep(2)
        self.session = aiohttp.ClientSession()
        logger.info(f"Modem {self.id} connected")

    async def disconnect(self):
        if self.session:
            await self.session.close()
        self.session = None
        logger.info(f"Modem {self.id} disconnected")

    async def send_request(self, request_data):
        if not self.session:
            await self.connect()
        
        try:
            async with self.session.request(
                method=request_data['method'],
                url=request_data['url'],
                headers=request_data['headers'],
                data=request_data['data']
            ) as response:
                return {
                    'status': response.status,
                    'headers': dict(response.headers),
                    'content': await response.read()
                }
        except Exception as e:
            logger.error(f"Error in modem {self.id}: {str(e)}")
            return {'error': str(e)}