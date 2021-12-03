from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.common.base.exception import NotFoundException
from app.modules.student.models import Student
from app.modules.teacher.models import Teacher
from app.setup.service import student_service, teacher_service

router = APIRouter()


class TeacherPost(BaseModel):
    name: str = Field(max_length=16)


@router.get("/teachers/{teacher_id}")
async def get_teacher(teacher_id: int) -> Teacher:
    teacher = await teacher_service.get_teacher(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return teacher


@router.get("/teachers/{teacher_id}/students")
async def get_students_of_teacher(teacher_id: int) -> list[Student]:
    try:
        students = await student_service.get_students_of_teacher(teacher_id)
    except NotFoundException:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return students


@router.post("/teachers")
async def post_teacher(teacher_post: TeacherPost) -> Teacher:
    teacher = await teacher_service.register_teacher(teacher_post.name)
    return teacher
