import asyncio

class EventBus:

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, handler):

        self.subscribers.setdefault(topic, []).append(handler)

    async def publish(self, topic, event):

        for handler in self.subscribers.get(topic, []):
            await handler(event)
