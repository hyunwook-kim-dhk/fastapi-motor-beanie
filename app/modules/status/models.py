from pydantic import BaseModel


class Status(BaseModel):
    version: str
