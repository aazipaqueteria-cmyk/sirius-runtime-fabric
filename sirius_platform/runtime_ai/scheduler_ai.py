class AIScheduler:

    def optimize(self, workload):

        if workload.get("latency") > 100:
            return "edge-node"

        return "core-cluster"
