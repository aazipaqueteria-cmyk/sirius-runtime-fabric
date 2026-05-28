class RuntimeDAG:

    def __init__(self):

        self.nodes = []

    def add_task(self, task):

        self.nodes.append(task)

    def tasks(self):

        return self.nodes
