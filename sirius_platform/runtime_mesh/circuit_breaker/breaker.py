class CircuitBreaker:

    def evaluate(self, failures):

        if failures >= 5:
            return "open"

        return "closed"
