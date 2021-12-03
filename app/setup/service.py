from app.modules.common.counter.counter import Counter
from app.modules.status.service import StatusService
from app.modules.student.repository import StudentRepository
from app.modules.student.service import StudentService
from app.modules.teacher.repository import TeacherRepository
from app.modules.teacher.service import TeacherService
from app.setup.database import db

status_service = StatusService()

counter = Counter(db)

teacher_repository = TeacherRepository(db, counter)
teacher_service = TeacherService(teacher_repository)

student_repository = StudentRepository(db, counter)
student_service = StudentService(teacher_repository, student_repository)
