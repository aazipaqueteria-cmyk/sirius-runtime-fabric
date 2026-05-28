class RuntimeTask:

    def __init__(self, name, payload):

        self.name = name
        self.payload = payload
        self.status = "pending"
