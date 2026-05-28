from pydantic import BaseModel

class RuntimeSettings(BaseModel):

    POSTGRES_DSN:str="postgresql+asyncpg://sirius:sirius@postgres:5432/sirius_runtime"
    REDIS_DSN:str="redis://redis:6379/0"
    NATS_URL:str="nats://nats:4222"
    API_HOST:str="0.0.0.0"
    API_PORT:int=8000

settings = RuntimeSettings()
