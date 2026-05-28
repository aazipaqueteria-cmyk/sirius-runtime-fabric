class RuntimeQueue:

    def __init__(self):
        self.jobs=[]

    def enqueue(self,job):
        self.jobs.append(job)

    def size(self):
        return len(self.jobs)
