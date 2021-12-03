from fastapi import APIRouter

from app.apis.v1.student.apis import router as student_router
from app.apis.v1.teacher.apis import router as teacher_router

router = APIRouter(prefix="/v1")

###########################################
# Add your routers here
###########################################
router.include_router(student_router)
router.include_router(teacher_router)
