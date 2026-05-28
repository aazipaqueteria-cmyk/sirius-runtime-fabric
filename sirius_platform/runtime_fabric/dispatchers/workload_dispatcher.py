class WorkloadDispatcher:

    def dispatch(self, workload):

        priority = workload.get("priority", "normal")
        tenant = workload.get("tenant", "free")

        if priority == "critical":
            return "dedicated-runtime"

        if tenant == "enterprise":
            return "isolated-cluster"

        if workload.get("gpu"):
            return "gpu-fabric"

        return "shared-runtime"
