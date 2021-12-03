from http import HTTPStatus

import pytest
from httpx import AsyncClient

from app.modules.student.service import StudentService
from app.modules.teacher.service import TeacherService


@pytest.mark.asyncio
async def test_get_teacher(http_client: AsyncClient, teacher_service: TeacherService) -> None:
    response = await http_client.get("/v1/teachers/12345")
    assert response.status_code == HTTPStatus.NOT_FOUND

    teacher = await teacher_service.register_teacher("teacher_name")

    response = await http_client.get(f"/v1/teachers/{teacher.teacher_id}")
    assert response.status_code == HTTPStatus.OK
    ret_teacher = response.json()
    assert ret_teacher["teacher_id"] == teacher.teacher_id
    assert ret_teacher["name"] == "teacher_name"


@pytest.mark.asyncio
async def test_get_students_of_teacher(
    http_client: AsyncClient, teacher_service: TeacherService, student_service: StudentService
) -> None:
    response = await http_client.get("/v1/teachers/12345/students")
    assert response.status_code == HTTPStatus.NOT_FOUND

    teacher = await teacher_service.register_teacher("teacher_name")
    response = await http_client.get(f"/v1/teachers/{teacher.teacher_id}/students")
    assert response.status_code == HTTPStatus.OK
    ret = response.json()
    assert isinstance(ret, list)
    assert len(ret) == 0

    await student_service.register_student(name="student_name", grade="A", teacher_id=teacher.teacher_id)
    await student_service.register_student(name="student_name", grade="A", teacher_id=teacher.teacher_id)
    await student_service.register_student(name="student_name", grade="A", teacher_id=teacher.teacher_id)
    response = await http_client.get(f"/v1/teachers/{teacher.teacher_id}/students")
    assert response.status_code == HTTPStatus.OK
    ret = response.json()
    assert isinstance(ret, list)
    assert len(ret) == 3
    assert ret[0]["teacher_id"] == 1
    assert ret[1]["teacher_id"] == 1
    assert ret[2]["teacher_id"] == 1


@pytest.mark.asyncio
async def test_post_teacher(http_client: AsyncClient) -> None:
    response = await http_client.post("/v1/teachers", json={"name": "teacher_name", "extra": "extra_value"})
    assert response.status_code == HTTPStatus.OK
