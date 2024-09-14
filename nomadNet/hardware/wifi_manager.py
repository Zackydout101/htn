import asyncio
from utils.logging import logger

class WiFiManager:
    def __init__(self, interface):
        self.interface = interface

    async def connect(self):
        # Simulate WiFi connection
        await asyncio.sleep(1)
        logger.info(f"WiFi connected on interface {self.interface}")

    async def upload(self, data):
        # Simulate data upload through WiFi
        await asyncio.sleep(len(data) / 1000000)  # Simulate 1 MB/s upload speed
        logger.info(f"Uploaded {len(data)} bytes through WiFi")