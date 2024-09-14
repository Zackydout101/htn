from typing import Dict
from hardware.lte_modem import LTEModem
from core.load_balancer import LoadBalancer
from networking.proxy_server import ProxyServer
from utils.logging import logger
from config.settings import LTE_MODEMS

class ProxyManager:
    def __init__(self, config):
        self.modems: Dict[str, LTEModem] = {}
        self.load_balancer = LoadBalancer()
        self.proxy_server = ProxyServer(self)

    async def initialize(self):
        for modem_config in LTE_MODEMS:
            modem = LTEModem(modem_config['id'], modem_config['interface'])
            await modem.connect()
            self.modems[modem_config['id']] = modem
            self.load_balancer.add_modem(modem)
        
        await self.proxy_server.start()

    async def get_proxy(self, domain: str) -> LTEModem:
        return self.load_balancer.get_modem(domain)

    async def refresh_ip(self, modem_id: str):
        modem = self.modems[modem_id]
        await modem.refresh_ip()