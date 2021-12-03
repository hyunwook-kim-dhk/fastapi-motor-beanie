from motor.motor_asyncio import AsyncIOMotorClient

from app.config.setting import SETTING

client = AsyncIOMotorClient(SETTING.MONGODB_URL)

db = client[SETTING.MONGODB_DBNAME]
