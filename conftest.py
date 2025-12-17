import pytest
from project_e2e.Api.objects import send_data, delete_data
from project_e2e.utils.payload import create_payload


@pytest.fixture
def created_object():
    """
    Create a new object and yield its ID and payload.
    """
    payload = create_payload()
    data = send_data(payload)
    assert data.status_code == 200
    yield data.json()["id"],payload
    delete_data(data.json()["id"])
