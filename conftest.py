import pytest
from project_e2e.Api.objects import send_data, delete_data
from project_e2e.utils.payload import create_payload, create_empty_payload


@pytest.fixture
def create_object():
    """
    Create a new object and yield its ID and payload.
    """
    payload = create_payload()
    data = send_data(payload)
    assert data.status_code == 200
    yield data.json()["id"], payload
    delete_data(data.json()["id"])


@pytest.fixture
def create_two_objects():
    """
    Create two new objects and yield their IDs
    """
    payload_1 = create_payload()
    payload_2 = create_payload()
    data_1 = send_data(payload_1)
    assert data_1.status_code == 200
    data_2 = send_data(payload_2)
    assert data_2.status_code == 200
    yield data_1.json()["id"], data_2.json()["id"]
    delete_data(data_1.json()["id"])
    delete_data(data_2.json()["id"])


@pytest.fixture
def create_empty_object():
    payload = create_empty_payload()
    data = send_data(payload)
    assert data.status_code == 200
    yield data.json()["id"], payload
    delete_data(data.json()["id"])


@pytest.fixture
def send_post_response():
    payload = create_payload()
    data = send_data(payload)
    assert data.status_code == 200
    yield data.json()
    delete_data(data.json()["id"])
