class WorkerNode:

    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity
        self.active=True

    def status(self):
        return {
            "node":self.name,
            "capacity":self.capacity,
            "active":self.active
        }
