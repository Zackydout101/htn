import netifaces
from utils.logging import logger

class LTEModem:
    def __init__(self, id, interface_name):
        self.id = id
        self.interface_name = interface_name
        self.ip_address = None

    async def connect(self):
        try:
            # Get the IP address of the interface
            addrs = netifaces.ifaddresses(self.interface_name)
            self.ip_address = addrs[netifaces.AF_INET][0]['addr']
            logger.info(f"Modem {self.id} connected on interface {self.interface_name} with IP {self.ip_address}")
        except Exception as e:
            logger.error(f"Error connecting modem {self.id}: {str(e)}")
            raise

    async def disconnect(self):
        self.ip_address = None
        logger.info(f"Modem {self.id} disconnected")

    async def refresh_ip(self):
        # This method would typically involve interacting with the modem to get a new IP
        # For Ethernet-connected LTE modems, this might involve sending AT commands
        # or using a modem-specific API. The exact implementation will depend on your modem.
        await self.disconnect()
        await self.connect()
        logger.info(f"IP refreshed for modem {self.id}. New IP: {self.ip_address}")