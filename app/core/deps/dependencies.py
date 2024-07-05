from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.database import Session


async def get_session():
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
