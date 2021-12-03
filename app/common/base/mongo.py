from datetime import datetime
from typing import Any, Callable, Generator

from bson.objectid import ObjectId as BsonObjectId
from pydantic import BaseModel, Field


class ObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls) -> Generator[Callable[[Any], "ObjectId"], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> "ObjectId":
        if not cls.is_valid(value):
            raise ValueError("Invalid ObjectId")  # pragma: no cover
        return cls(value)

    @classmethod
    def __modify_schema__(cls, field_schema: Any) -> None:
        field_schema.update(type="string")  # pragma: no cover


class MongoDoc(BaseModel):
    id: ObjectId = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime
