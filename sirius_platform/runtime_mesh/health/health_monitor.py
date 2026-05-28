class HealthMonitor:

    def validate(self,node):

        if not node.active:
            return "unhealthy"

        return "healthy"
