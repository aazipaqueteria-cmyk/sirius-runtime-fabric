from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://sirius:sirius@postgres:5432/sirius_runtime"

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True
)
