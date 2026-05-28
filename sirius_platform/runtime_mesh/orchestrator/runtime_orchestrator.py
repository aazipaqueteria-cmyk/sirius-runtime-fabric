class RuntimeOrchestrator:

    def allocate(self, workload):

        if workload.get("priority") == "critical":
            return "priority-node"

        return "shared-node"
