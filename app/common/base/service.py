from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    async def setup(self) -> None:
        pass
