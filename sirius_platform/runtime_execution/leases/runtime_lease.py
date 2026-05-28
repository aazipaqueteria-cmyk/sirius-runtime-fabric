import time

class RuntimeLease:

    def __init__(self, worker, ttl=30):

        self.worker = worker
        self.ttl = ttl
        self.timestamp = time.time()

    def active(self):

        return (time.time() - self.timestamp) < self.ttl
