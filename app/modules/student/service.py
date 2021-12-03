from typing import Optional

from app.common.base.exception import NotFoundException
from app.common.base.service import BaseService
from app.modules.student.models import Student
from app.modules.student.repository import StudentRepository
from app.modules.teacher.repository import TeacherRepository


class StudentService(BaseService):
    teacher_repository: TeacherRepository
    student_repository: StudentRepository

    def __init__(self, teacher_repository: TeacherRepository, student_repository: StudentRepository) -> None:
        self.teacher_repository = teacher_repository
        self.student_repository = student_repository

    async def setup(self) -> None:
        # No additional setup required
        pass

    async def register_student(self, name: str, grade: str, teacher_id: int) -> Student:
        teacher_doc = await self.teacher_repository.find_one_by_teacher_id(teacher_id)
        if teacher_doc is None:
            raise NotFoundException(f"TeacherDoc(teacher_id={teacher_id}) does not exist.")
        inserted = await self.student_repository.insert_one(name=name, grade=grade, teacher_id=teacher_id)
        return Student(**inserted.dict())

    async def get_student(self, student_id: int) -> Optional[Student]:
        found = await self.student_repository.find_one_by_student_id(student_id)
        if found is None:
            return None
        return Student(**found.dict())

    async def get_students_of_teacher(self, teacher_id: int) -> list[Student]:
        teacher_doc = await self.teacher_repository.find_one_by_teacher_id(teacher_id)
        if teacher_doc is None:
            raise NotFoundException(f"TeacherDoc(teacher_id={teacher_id}) does not exist.")
        founds = await self.student_repository.find_by_teacher_id(teacher_id)
        return [Student(**found.dict()) for found in founds]
