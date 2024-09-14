import asyncio

class IPRefresher:
    async def refresh(self, modem):
        await modem.disconnect()
        await asyncio.sleep(5)  # Wait for 5 seconds
        await modem.connect()