from datetime import datetime
from logging import getLogger
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorDatabase

from app.common.base.exception import DomainException
from app.common.base.repository import BaseRepository
from app.modules.common.counter.counter import Counter
from app.modules.teacher.docs import TeacherDoc

logger = getLogger(__name__)


class TeacherRepository(BaseRepository):
    _counter: Counter

    def __init__(self, db: AsyncIOMotorDatabase, counter: Counter) -> None:
        super().__init__(db, "teachers")
        self._counter = counter

    async def setup_indexes(self) -> None:
        self._collection.create_index("teacher_id")

    async def insert_one(self, name: str) -> TeacherDoc:
        teacher_id = await self._counter.next(self._collection_name)
        now = datetime.now()
        await self._collection.insert_one(
            {
                "teacher_id": teacher_id,
                "name": name,
                "created_at": now,
                "updated_at": now,
            }
        )
        found = await self.find_one_by_teacher_id(teacher_id)
        if found is None:  # pragma: no cover
            raise DomainException()
        return found

    async def find_one_by_teacher_id(self, teacher_id: int) -> Optional[TeacherDoc]:
        found = await self._collection.find_one({"teacher_id": teacher_id})
        if found is None:
            return None
        return TeacherDoc(**found)
