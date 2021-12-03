import pytest

from app.modules.teacher.repository import TeacherRepository


@pytest.mark.asyncio
async def test_insert_one(teacher_repository: TeacherRepository) -> None:
    teacher_doc = await teacher_repository.insert_one("teacher_name")
    assert teacher_doc.id is not None
    assert teacher_doc.teacher_id == 1
    assert teacher_doc.name == "teacher_name"
    assert teacher_doc.created_at is not None
    assert teacher_doc.updated_at is not None


@pytest.mark.asyncio
async def test_find_one_by_teacher_id(teacher_repository: TeacherRepository) -> None:
    ret = await teacher_repository.find_one_by_teacher_id(teacher_id=12345)
    assert ret is None

    teacher_doc = await teacher_repository.insert_one("teacher_name")
    ret = await teacher_repository.find_one_by_teacher_id(teacher_id=teacher_doc.teacher_id)
    assert ret is not None
    assert ret.id == teacher_doc.id
    assert ret.teacher_id == teacher_doc.teacher_id
    assert teacher_doc.name == teacher_doc.name
    assert teacher_doc.created_at is not None
    assert teacher_doc.updated_at is not None
