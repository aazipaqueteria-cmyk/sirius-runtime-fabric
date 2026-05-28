class ServiceRegistry:

    def __init__(self):
        self.services = {}

    def register(self,name,host):

        self.services[name]=host

    def resolve(self,name):

        return self.services.get(name)
