from app.common.base.mongo import MongoDoc


class TeacherDoc(MongoDoc):
    teacher_id: int
    name: str
