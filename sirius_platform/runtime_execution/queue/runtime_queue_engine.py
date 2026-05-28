class RuntimeQueueEngine:

    def __init__(self):

        self.queue = []

    def enqueue(self, item):

        self.queue.append(item)

    def dequeue(self):

        if self.queue:
            return self.queue.pop(0)
