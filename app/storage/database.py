from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings


client = AsyncIOMotorClient(settings.DATABASE_URL)


async def get_database() -> AsyncIOMotorClient:
    return client
