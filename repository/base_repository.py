from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base
from typing import Optional
from config.settings import settings

Base = declarative_base()
engine = create_async_engine(
    settings.DB_URL,
    pool_size=10,
    echo=True,
    pool_pre_ping=True,
    autocommit=False
)
1

async def get_db_session() -> AsyncSession:
    sess = AsyncSession(bind=engine)
    try:
        yield sess
    finally:
        await sess.close()