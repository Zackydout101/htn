import asyncio
from typing import Dict, List
from hardware.lte_modem import LTEModem
from hardware.wifi_manager import WiFiManager
from core.load_balancer import LoadBalancer
from core.ip_refresher import IPRefresher
from networking.proxy_server import ProxyServer
from utils.logging import logger
from config.settings import LTE_MODEMS

class ProxyManager:
    def __init__(self, config):
        self.modems: Dict[str, LTEModem] = {}
        self.wifi = WiFiManager(config['WIFI_INTERFACE'])
        self.load_balancer = LoadBalancer()
        self.ip_refresher = IPRefresher()
        self.proxy_server = ProxyServer(self)

    async def initialize(self):
        for modem_config in LTE_MODEMS:
            modem = LTEModem(modem_config['id'], modem_config['device'])
            await modem.connect()
            self.modems[modem_config['id']] = modem
            self.load_balancer.add_modem(modem)
        
        await self.wifi.connect()
        await self.proxy_server.start()

    async def get_proxy(self, domain: str) -> LTEModem:
        return self.load_balancer.get_modem(domain)

    async def refresh_ip(self, modem_id: str):
        modem = self.modems[modem_id]
        await self.ip_refresher.refresh(modem)

    async def handle_request(self, request_data: dict) -> dict:
        modem = await self.get_proxy(request_data['domain'])
        response = await modem.send_request(request_data)
        return response

    async def upload_data(self, data: bytes) -> None:
        await self.wifi.upload(data)
