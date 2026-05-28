import hashlib

class IdempotencyKey:

    def generate(self, payload):

        return hashlib.sha256(
            str(payload).encode()
        ).hexdigest()
