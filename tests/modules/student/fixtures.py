from typing import AsyncGenerator

import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.modules.common.counter.counter import Counter
from app.modules.student.repository import StudentRepository
from app.modules.student.service import StudentService
from app.modules.teacher.repository import TeacherRepository


@pytest.fixture
async def student_service(motor_db: AsyncIOMotorDatabase) -> AsyncGenerator[StudentService, None]:
    counter = Counter(motor_db)
    teacher_repository = TeacherRepository(motor_db, counter)
    student_repository = StudentRepository(motor_db, counter)
    yield StudentService(teacher_repository, student_repository)


@pytest.fixture
async def student_repository(motor_db: AsyncIOMotorDatabase) -> AsyncGenerator[StudentRepository, None]:
    counter = Counter(motor_db)
    await counter.setup_indexes()
    student_repository = StudentRepository(motor_db, counter)
    await student_repository.setup_indexes()
    yield student_repository
