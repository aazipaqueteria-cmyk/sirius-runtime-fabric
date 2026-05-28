class DeadLetterQueue:

    def push(self,event):

        return {
            "status":"stored",
            "event":event
        }
