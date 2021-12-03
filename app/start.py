from logging import getLogger

from fastapi import FastAPI

from app.apis.common.routes import router as common_router
from app.apis.v1.routes import router as v1_router
from app.common.util.logger import LogLevel, setup_logger
from app.common.util.version import get_project_version
from app.config.setting import SETTING
from app.setup.middleware import middlewares
from app.setup.service import student_service, teacher_service

setup_logger(LogLevel[SETTING.LOG_LEVEL])

logger = getLogger(__name__)


app = FastAPI(
    version=get_project_version(),
    middleware=middlewares,
)
app.include_router(common_router)
app.include_router(v1_router)


@app.on_event("startup")
async def startup() -> None:
    logger.info("FastAPI is now starting up.")

    logger.info("StudentService started to setup")
    await student_service.setup()

    logger.info("TeacherService started to setup")
    await teacher_service.setup()


@app.on_event("shutdown")
async def shutdown() -> None:
    logger.info("FastAPI is now shutting down.")
