from datetime import datetime
from logging import getLogger
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorDatabase

from app.common.base.exception import DomainException
from app.common.base.repository import BaseRepository
from app.modules.common.counter.counter import Counter
from app.modules.student.docs import StudentDoc

logger = getLogger(__name__)


class StudentRepository(BaseRepository):
    _counter: Counter

    def __init__(self, db: AsyncIOMotorDatabase, counter: Counter) -> None:
        super().__init__(db, "students")
        self._counter = counter

    async def setup_indexes(self) -> None:
        await self._collection.create_index("student_id")
        await self._collection.create_index("teacher_id")

    async def insert_one(self, name: str, grade: str, teacher_id: int) -> StudentDoc:
        student_id = await self._counter.next(self._collection_name)
        now = datetime.now()
        await self._collection.insert_one(
            {
                "student_id": student_id,
                "name": name,
                "grade": grade,
                "teacher_id": teacher_id,
                "created_at": now,
                "updated_at": now,
            }
        )
        found = await self.find_one_by_student_id(student_id)
        if found is None:  # pragma: no cover
            raise DomainException()
        return found

    async def find_one_by_student_id(self, student_id: int) -> Optional[StudentDoc]:
        found = await self._collection.find_one({"student_id": student_id})
        if found is None:
            return None
        return StudentDoc(**found)

    async def find_by_teacher_id(self, teacher_id: int) -> list[StudentDoc]:
        cursor = self._collection.find({"teacher_id": teacher_id})
        founds = await cursor.to_list(None)
        return [StudentDoc(**found) for found in founds]
