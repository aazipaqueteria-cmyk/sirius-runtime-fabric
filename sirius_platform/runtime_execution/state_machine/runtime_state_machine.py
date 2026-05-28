class RuntimeStateMachine:

    VALID = [
        "pending",
        "running",
        "retrying",
        "failed",
        "completed"
    ]

    def transition(self, state):

        return state in self.VALID
