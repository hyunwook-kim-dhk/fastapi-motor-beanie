from abc import ABC, abstractmethod

from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase


class BaseRepository(ABC):
    _collection_name: str
    _collection: AsyncIOMotorCollection

    def __init__(self, db: AsyncIOMotorDatabase, collection_name: str) -> None:
        self._collection_name = collection_name
        self._collection = db[collection_name]

    @abstractmethod
    async def setup_indexes(self) -> None:
        pass
