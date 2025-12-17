import pytest

from project_e2e.Api.objects import get_data, full_update, partial_update, delete_data
from project_e2e.utils.payload import create_payload

@pytest.mark.e2e
def test_e2e(created_object):
    """
    Test the end-to-end flow for creating, updating, partial updating, deleting, and failure response.
    """
    object_id,payload = created_object

    # initial payload validation
    get_response = get_data(object_id)
    assert get_response.status_code == 200
    assert get_response.json().get("name") == payload["name"]
    assert get_response.json().get("data") == payload["data"]

    # updating the payload and validating
    new_payload = create_payload()
    update_response = full_update(object_id,new_payload)
    assert update_response.status_code == 200
    assert "updatedAt" in update_response.json()
    get_updated_response = get_data(object_id)
    assert get_updated_response.status_code == 200
    assert get_updated_response.json().get("name") == new_payload["name"]
    assert get_updated_response.json().get("data") == new_payload["data"]

    # partial update and validation
    patched_payload = {
        "data": {
            "price": 1500.00
        }
    }
    patch_response = partial_update(object_id,patched_payload)
    assert patch_response.status_code == 200
    assert "updatedAt" in patch_response.json()

    get_patched_response = get_data(object_id)
    assert get_patched_response.status_code == 200
    # PATCH replaces entire data object for this API
    assert get_patched_response.json()["name"] == new_payload["name"]
    assert get_patched_response.json()["data"] == patched_payload["data"]

    # delete response validation
    delete_response = delete_data(object_id)
    assert delete_response.status_code == 200

    # failure response validation
    failure_response = get_data(object_id)
    assert failure_response.status_code == 404




