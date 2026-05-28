class DistributedScheduler:

    def schedule(self, workload):

        if workload.get("priority") == "critical":
            return "dedicated-cluster"

        if workload.get("gpu"):
            return "gpu-cluster"

        return "shared-cluster"
