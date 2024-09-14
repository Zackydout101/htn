import time
from collections import defaultdict

class Metrics:
    def __init__(self):
        self.request_times = defaultdict(list)
        self.request_counts = defaultdict(int)

    def record_request(self, modem_id, duration):
        self.request_times[modem_id].append(duration)
        self.request_counts[modem_id] += 1

    def get_average_time(self, modem_id):
        times = self.request_times[modem_id]
        return sum(times) / len(times) if times else 0

    def get_request_count(self, modem_id):
        return self.request_counts[modem_id]