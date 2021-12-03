from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.common.base.exception import NotFoundException
from app.modules.student.models import Student
from app.setup.service import student_service

NAME_FIELD = Field(max_length=16)
GRADE_FIELD = Field(max_length=4)


class StudentPost(BaseModel):
    name: str = NAME_FIELD
    grade: str = GRADE_FIELD
    teacher_id: int


class StudentPatch(BaseModel):
    grade: str = GRADE_FIELD


router = APIRouter()


@router.get("/students/{student_id}")
async def get_student(student_id: int) -> Student:
    student = await student_service.get_student(student_id=student_id)
    if student is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return student


@router.post("/students")
async def post_student(student_post: StudentPost) -> Student:
    try:
        student = await student_service.register_student(
            name=student_post.name, grade=student_post.grade, teacher_id=student_post.teacher_id
        )
    except NotFoundException:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return student
