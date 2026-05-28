class PolicyEngine:

    RULES = {
        "free":["read"],
        "pro":["read","write"],
        "enterprise":["read","write","execute"]
    }

    def allowed(self, tenant, action):
        return action in self.RULES.get(tenant,[])
