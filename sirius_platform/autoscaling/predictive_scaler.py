class PredictiveScaler:

    def scale(self,cpu):

        if cpu > 80:
            return "scale_up"

        if cpu < 20:
            return "scale_down"

        return "stable"
