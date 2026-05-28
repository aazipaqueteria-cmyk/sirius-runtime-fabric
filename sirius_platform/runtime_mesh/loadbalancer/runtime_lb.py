class RuntimeLoadBalancer:

    def select(self, nodes):

        if not nodes:
            return None

        return nodes[0]
