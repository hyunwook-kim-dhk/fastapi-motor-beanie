import pytest

from app.modules.student.repository import StudentRepository


@pytest.mark.asyncio
async def test_insert_one(student_repository: StudentRepository) -> None:
    student_doc = await student_repository.insert_one(name="student_name", grade="A", teacher_id=1)
    assert student_doc.id is not None
    assert student_doc.student_id == 1
    assert student_doc.name == "student_name"
    assert student_doc.grade == "A"
    assert student_doc.teacher_id == 1


@pytest.mark.asyncio
async def test_find_one_by_student_id(student_repository: StudentRepository) -> None:
    ret = await student_repository.find_one_by_student_id(12345)
    assert ret is None

    student_doc = await student_repository.insert_one(name="student_name", grade="A", teacher_id=1)
    ret = await student_repository.find_one_by_student_id(student_doc.student_id)
    assert ret is not None
    assert ret.id is not None
    assert ret.student_id == 1
    assert ret.name == "student_name"
    assert ret.grade == "A"
    assert ret.teacher_id == 1


@pytest.mark.asyncio
async def test_find_by_teacher_id(student_repository: StudentRepository) -> None:
    ret = await student_repository.find_by_teacher_id(12345)
    assert len(ret) == 0

    await student_repository.insert_one(name="student_name", grade="A", teacher_id=1)
    await student_repository.insert_one(name="student_name", grade="A", teacher_id=1)
    await student_repository.insert_one(name="student_name", grade="A", teacher_id=1)
    ret = await student_repository.find_by_teacher_id(1)
    assert len(ret) == 3
