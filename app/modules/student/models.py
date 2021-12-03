from pydantic import BaseModel


class Student(BaseModel):
    student_id: int
    name: str
    grade: str
    teacher_id: int
