import pytest
from pytest_mock_resources import create_mongo_fixture
from conftest import async_app_client


@pytest.mark.asyncio
async def test_create_record(async_app_client):
    response = await async_app_client.post("/record", json={
        "trial_sequence": "0",
        "trial_id": "0",
        "trial_category": "cat",
        "time": "10000",
        "pupil_dia_x": "2.20",
        "pupil_dia_y": "9.01",
        "gaze_pos_x": "2",
        "gaze_pos_y": "4"
    })

    assert response.status_code == 200, response.text
