from typing import AsyncGenerator

import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.modules.common.counter.counter import Counter
from app.modules.teacher.repository import TeacherRepository
from app.modules.teacher.service import TeacherService


@pytest.fixture
async def teacher_repository(motor_db: AsyncIOMotorDatabase) -> AsyncGenerator[TeacherRepository, None]:
    counter = Counter(motor_db)
    await counter.setup_indexes()
    teacher_repository = TeacherRepository(motor_db, counter)
    await teacher_repository.setup_indexes()
    yield teacher_repository


@pytest.fixture
async def teacher_service(motor_db: AsyncIOMotorDatabase) -> AsyncGenerator[TeacherService, None]:
    counter = Counter(motor_db)
    teacher_repository = TeacherRepository(motor_db, counter)
    yield TeacherService(teacher_repository)
