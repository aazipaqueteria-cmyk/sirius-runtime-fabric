class RuntimeRecovery:

    def recover(self,node):

        node.active=True

        return {
            "node":node.name,
            "recovered":True
        }
