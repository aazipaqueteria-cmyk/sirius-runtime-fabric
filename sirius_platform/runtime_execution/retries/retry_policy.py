class RetryPolicy:

    def allowed(self, retries):

        return retries < 3
