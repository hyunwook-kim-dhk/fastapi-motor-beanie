from app.common.base.mongo import MongoDoc


class StudentDoc(MongoDoc):
    student_id: int
    name: str
    grade: str
    teacher_id: int
