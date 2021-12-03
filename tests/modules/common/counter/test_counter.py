from uuid import uuid4

import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from app.modules.common.counter.counter import Counter


@pytest.mark.asyncio
async def test_next(motor_db: AsyncIOMotorClient) -> None:
    counter = Counter(motor_db)
    random_counter_name = str(uuid4())
    ret = await counter.next(random_counter_name)
    assert ret == 1
    ret = await counter.next(random_counter_name)
    assert ret == 2
