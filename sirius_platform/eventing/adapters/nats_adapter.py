class NatsAdapter:

    async def publish(self, topic, payload):

        return {
            "broker":"nats",
            "topic":topic,
            "status":"published"
        }
