import nats

class RuntimeEventBus:

    async def connect(self):

        return await nats.connect(
            servers=["nats://nats:4222"]
        )
