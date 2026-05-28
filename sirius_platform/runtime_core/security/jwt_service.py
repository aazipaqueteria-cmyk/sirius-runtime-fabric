import secrets

class JWTService:

    def issue(self,user):

        return {
            "token":secrets.token_hex(32),
            "user":user
        }
