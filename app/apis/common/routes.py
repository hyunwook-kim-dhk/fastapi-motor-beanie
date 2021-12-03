from fastapi import APIRouter

from app.apis.common.status.apis import router as status_router

router = APIRouter()

router.include_router(status_router)
