class RuntimeCoordinator:

    def assign(self, workload):

        if workload.get("critical"):
            return "priority-worker"

        return "shared-worker"
