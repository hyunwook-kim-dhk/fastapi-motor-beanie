import pytest

from app.modules.teacher.service import TeacherService


@pytest.mark.asyncio
async def test_register_teacher(teacher_service: TeacherService) -> None:
    teacher = await teacher_service.register_teacher("teacher_name")
    assert teacher.teacher_id == 1
    assert teacher.name == "teacher_name"


@pytest.mark.asyncio
async def test_get_teacher(teacher_service: TeacherService) -> None:
    ret = await teacher_service.get_teacher(12345)
    assert ret is None

    teacher = await teacher_service.register_teacher("teacher_name")
    ret = await teacher_service.get_teacher(teacher.teacher_id)
    assert ret is not None
    assert ret.teacher_id == teacher.teacher_id
    assert ret.name == teacher.name
