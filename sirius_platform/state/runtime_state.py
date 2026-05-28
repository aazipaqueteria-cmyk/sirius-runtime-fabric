class RuntimeState:

    def __init__(self):
        self.state = {}

    def set(self,key,val):
        self.state[key]=val

    def get(self,key):
        return self.state.get(key)
