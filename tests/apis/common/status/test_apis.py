import re
from http import HTTPStatus

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_status(http_client: AsyncClient) -> None:
    response = await http_client.get("/")
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert re.match(r"\d+\.\d+\.\d+-?.*", data["version"])  # Check semver format
