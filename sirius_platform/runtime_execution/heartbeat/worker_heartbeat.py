import time

class WorkerHeartbeat:

    def beat(self, worker):

        return {
            "worker":worker,
            "timestamp":time.time(),
            "status":"alive"
        }
