from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import sessionmaker

from app.core.config.config import settings

engine: AsyncEngine = create_async_engine(
    settings.CONNECTION_SCHEMA.unicode_string(), echo=True, future=True
)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
