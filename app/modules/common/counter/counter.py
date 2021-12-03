from motor.motor_asyncio import AsyncIOMotorDatabase

from app.common.base.repository import BaseRepository


class Counter(BaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        super().__init__(db, "counters")

    async def setup_indexes(self) -> None:
        await self._collection.create_index("name")

    async def next(self, name: str) -> int:
        counter_doc = await self._collection.find_one_and_update(
            {"name": name},
            {"$inc": {"count": 1}},
            return_document=True,
            upsert=True,
        )
        return int(counter_doc["count"])
