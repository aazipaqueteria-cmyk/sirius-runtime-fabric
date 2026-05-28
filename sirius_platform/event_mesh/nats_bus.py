class EventBus:

    def publish(self, topic, payload):
        print(f"[EVENT] {topic} -> {payload}")
