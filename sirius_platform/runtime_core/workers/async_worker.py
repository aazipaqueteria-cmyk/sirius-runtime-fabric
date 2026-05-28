import asyncio

class AsyncWorker:

    async def execute(self, task):

        await asyncio.sleep(0.1)

        return {
            "task":task,
            "status":"completed"
        }
