class RuntimeEvent:

    def emit(self, event):

        return {
            "event":event,
            "status":"emitted"
        }
