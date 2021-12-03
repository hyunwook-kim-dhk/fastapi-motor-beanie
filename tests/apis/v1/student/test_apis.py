from http import HTTPStatus

import pytest
from httpx import AsyncClient

from app.modules.student.service import StudentService
from app.modules.teacher.service import TeacherService


@pytest.mark.asyncio
async def test_get_student(
    http_client: AsyncClient, teacher_service: TeacherService, student_service: StudentService
) -> None:
    response = await http_client.get("/v1/students/12345")
    assert response.status_code == HTTPStatus.NOT_FOUND

    teacher = await teacher_service.register_teacher("teacher_name")
    student = await student_service.register_student("student_name", "A", teacher.teacher_id)

    response = await http_client.get(f"/v1/students/{student.student_id}")
    assert response.status_code == HTTPStatus.OK
    ret_student = response.json()
    assert ret_student["student_id"] == student.student_id
    assert ret_student["name"] == "student_name"
    assert ret_student["grade"] == "A"
    assert ret_student["teacher_id"] == teacher.teacher_id


@pytest.mark.asyncio
async def test_post_student(http_client: AsyncClient, teacher_service: TeacherService) -> None:
    response = await http_client.post(
        "/v1/students",
        json={
            # "name" is missing
            "grade": "A",
            "teacher_id": 12345,
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    response = await http_client.post(
        "/v1/students",
        json={
            "name": "test_student",
            # "grade" is missing
            "teacher_id": 12345,
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    response = await http_client.post(
        "/v1/students",
        json={
            "name": "test_student",
            "grade": "A",
            # "teacher_id" is missing
        },
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    response = await http_client.post("/v1/students", json={"name": "test_student", "grade": "A", "teacher_id": 12345})
    assert response.status_code == HTTPStatus.NOT_FOUND

    teacher = await teacher_service.register_teacher("teacher_name")

    response = await http_client.post(
        "/v1/students", json={"name": "test_student", "grade": "A", "teacher_id": teacher.teacher_id}
    )
    assert response.status_code == HTTPStatus.OK

    json = response.json()
    assert json["student_id"] == 1
    assert json["name"] == "test_student"
    assert json["grade"] == "A"
    assert json["teacher_id"] == teacher.teacher_id
