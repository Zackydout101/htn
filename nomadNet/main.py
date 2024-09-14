import asyncio
from config.settings import *
from core.proxy_manager import ProxyManager

async def main():
    proxy_manager = ProxyManager({
        'LTE_MODEMS': LTE_MODEMS,
        'WIFI_INTERFACE': WIFI_INTERFACE,
        'MAX_CONNECTIONS_PER_MODEM': MAX_CONNECTIONS_PER_MODEM,
        'IP_REFRESH_INTERVAL': IP_REFRESH_INTERVAL,
        'AUTH_TOKEN': AUTH_TOKEN,
        'LOG_FILE': LOG_FILE
    })

    await proxy_manager.initialize()

    # Keep the server running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())