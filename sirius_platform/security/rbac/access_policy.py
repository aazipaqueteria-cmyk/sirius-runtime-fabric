class AccessPolicy:

    def allowed(self,role,resource):

        if role == "admin":
            return True

        return False
