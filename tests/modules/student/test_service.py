import pytest

from app.common.base.exception import NotFoundException
from app.modules.student.service import StudentService
from app.modules.teacher.service import TeacherService


@pytest.mark.asyncio
async def test_register_student(teacher_service: TeacherService, student_service: StudentService) -> None:
    with pytest.raises(NotFoundException):
        await student_service.register_student("student_name", "A", 12345)

    teacher = await teacher_service.register_teacher("teacher_name")
    student = await student_service.register_student("student_name", "A", teacher.teacher_id)
    assert student.student_id == 1
    assert student.name == "student_name"
    assert student.grade == "A"
    assert student.teacher_id == teacher.teacher_id


@pytest.mark.asyncio
async def test_get_student(teacher_service: TeacherService, student_service: StudentService) -> None:
    ret = await student_service.get_student(12345)
    assert ret is None

    teacher = await teacher_service.register_teacher("teacher_name")
    student = await student_service.register_student("student_name", "A", teacher.teacher_id)

    ret = await student_service.get_student(student.student_id)
    assert ret is not None
    assert ret.student_id == 1
    assert ret.name == "student_name"
    assert ret.grade == "A"
    assert ret.teacher_id == teacher.teacher_id


@pytest.mark.asyncio
async def test_get_students_of_teacher(teacher_service: TeacherService, student_service: StudentService) -> None:
    with pytest.raises(NotFoundException):
        await student_service.get_students_of_teacher(12345)

    teacher = await teacher_service.register_teacher("teacher_name")
    await student_service.register_student("student_name", "A", teacher.teacher_id)

    ret = await student_service.get_students_of_teacher(teacher.teacher_id)
    assert len(ret) == 1

    await student_service.register_student("student_name", "A", teacher.teacher_id)
    await student_service.register_student("student_name", "A", teacher.teacher_id)
    ret = await student_service.get_students_of_teacher(teacher.teacher_id)
    assert len(ret) == 3
    assert ret[0].name == "student_name"
    assert ret[0].grade == "A"
    assert ret[0].teacher_id == teacher.teacher_id
