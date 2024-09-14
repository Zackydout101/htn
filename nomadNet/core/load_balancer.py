from collections import defaultdict
from config.settings import MAX_CONNECTIONS_PER_MODEM
import time

class LoadBalancer:
    def __init__(self):
        self.modems = []
        self.domain_usage = defaultdict(lambda: defaultdict(int))
        self.last_used = {}

    def add_modem(self, modem):
        self.modems.append(modem)
        self.last_used[modem.id] = 0

    def get_modem(self, domain):
        current_time = time.time()
        
        # Find the least recently used modem
        lru_modem = min(self.modems, key=lambda m: self.last_used[m.id])
        
        # Check if this modem has been overused for this domain
        if self.domain_usage[domain][lru_modem.id] < MAX_CONNECTIONS_PER_MODEM:
            self.domain_usage[domain][lru_modem.id] += 1
            self.last_used[lru_modem.id] = current_time
            return lru_modem
        
        # If overused, find the next best modem
        for modem in sorted(self.modems, key=lambda m: self.last_used[m.id]):
            if self.domain_usage[domain][modem.id] < MAX_CONNECTIONS_PER_MODEM:
                self.domain_usage[domain][modem.id] += 1
                self.last_used[modem.id] = current_time
                return modem
        
        # If all modems are overused, return the least recently used one
        self.last_used[lru_modem.id] = current_time
        return lru_modem