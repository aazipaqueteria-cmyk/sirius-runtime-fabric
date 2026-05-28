from collections import defaultdict

class RuntimeMetrics:

    def __init__(self):
        self.metrics = defaultdict(int)

    def increment(self,key):
        self.metrics[key]+=1

    def export(self):
        return dict(self.metrics)
