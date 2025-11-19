from httpx import AsyncClient
import pytest

from api import app


@pytest.fixture
async def async_app_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
