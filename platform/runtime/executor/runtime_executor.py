class RuntimeExecutor:

    def execute(self, workload):

        tenant = workload.get("tenant")

        if tenant == "enterprise":
            runtime = "isolated-runtime"
        else:
            runtime = "shared-runtime"

        return {
            "status":"accepted",
            "runtime":runtime,
            "task":workload.get("task")
        }
