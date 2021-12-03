from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_app_init(http_client: AsyncClient) -> None:
    response = await http_client.get("/")
    assert response.status_code == HTTPStatus.OK
