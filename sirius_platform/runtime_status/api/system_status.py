import platform
import os
import time

class SystemStatus:

    def health(self):

        return {
            "runtime":"active",
            "hostname":platform.node(),
            "os":platform.system(),
            "cpu_count":os.cpu_count(),
            "timestamp":time.time()
        }
