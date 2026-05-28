class StateReplication:

    def replicate(self,data,target):

        return {
            "target":target,
            "replicated":True,
            "payload":data
        }
