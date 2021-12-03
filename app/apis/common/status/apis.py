from fastapi import APIRouter
from pydantic import BaseModel

from app.setup.service import status_service


class StatusResponse(BaseModel):
    version: str


router = APIRouter()


@router.get("/")
async def get_status() -> StatusResponse:
    status = await status_service.get_status()
    return StatusResponse(**status.dict())


# TODO: Add health check apis here # pylint: disable=fixme
