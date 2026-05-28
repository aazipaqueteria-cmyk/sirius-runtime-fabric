class RuntimeWorker:

    def execute(self, task):

        task.status = "completed"

        return task
