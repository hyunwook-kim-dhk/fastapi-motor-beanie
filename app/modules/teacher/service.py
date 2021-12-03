from typing import Optional

from app.common.base.service import BaseService
from app.modules.teacher.models import Teacher
from app.modules.teacher.repository import TeacherRepository


class TeacherService(BaseService):
    teacher_repository: TeacherRepository

    def __init__(self, teacher_repository: TeacherRepository) -> None:
        self.teacher_repository = teacher_repository

    async def setup(self) -> None:
        # No additional setup required
        pass

    async def register_teacher(self, name: str) -> Teacher:
        inserted = await self.teacher_repository.insert_one(name=name)
        return Teacher(**inserted.dict())

    async def get_teacher(self, teacher_id: int) -> Optional[Teacher]:
        found = await self.teacher_repository.find_one_by_teacher_id(teacher_id)
        if found is None:
            return None
        return Teacher(**found.dict())
