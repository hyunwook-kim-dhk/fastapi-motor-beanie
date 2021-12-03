from app.common.base.service import BaseService
from app.common.util.version import get_project_version
from app.modules.status.models import Status


class StatusService(BaseService):
    _version: str

    def __init__(self) -> None:
        self._version = get_project_version()

    async def setup(self) -> None:
        # No additional setup required.
        pass

    async def get_status(self) -> Status:
        return Status(version=self._version)
