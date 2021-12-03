from pydantic import BaseModel


class Teacher(BaseModel):
    teacher_id: int
    name: str
