import asyncio
from asyncio import AbstractEventLoop
from logging import getLogger
from typing import AsyncGenerator, Generator

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config.setting import SETTING
from app.start import app as _app

logger = getLogger(__name__)


@pytest.fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app() -> Generator[FastAPI, None, None]:
    yield _app


@pytest.fixture
async def http_client(app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as async_client, LifespanManager(app=app):
        yield async_client


@pytest.fixture
async def motor_client() -> AsyncGenerator[AsyncIOMotorClient, None]:
    client = AsyncIOMotorClient(SETTING.MONGODB_URL)
    yield client


@pytest.fixture
async def motor_db(motor_client: AsyncIOMotorClient) -> AsyncGenerator[AsyncIOMotorDatabase, None]:
    db = motor_client[SETTING.MONGODB_DBNAME]
    for collection_name in await db.list_collection_names():
        await db[collection_name].drop()
    yield db
