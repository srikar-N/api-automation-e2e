import random

import pytest

from project_e2e.Api.objects import get_data, send_invalid_json, send_data, full_update, partial_update, \
    full_update_with_header
from project_e2e.utils.payload import create_payload


@pytest.mark.negative
def test_non_existent_resource():
    """
    checking the APi response for Invalid ID
    """

    random_id = random.randint(900000000000000, 1000000000000000)
    invalid_response = get_data(str(random_id))
    assert invalid_response.status_code == 404


@pytest.mark.negative
def test_invalid_payload_request():
    """
    Testing the API response for invalid JSON request
    """
    payload = "Helloworld"
    invalid_json_response = send_invalid_json(payload)
    assert invalid_json_response.status_code in range(400, 500)


@pytest.mark.negative
def test_no_required_field():
    """
    Testing the API response if some of the fields are ignored in payload
    """
    payload = {
        "data": {
            "year": random.randint(2015, 2024),
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = send_data(payload)
    if response.status_code == 200:
        assert None == response.json()["name"]
    elif response.status_code in range(400, 500):
        assert "error" in response.json()


@pytest.mark.negative
def test_non_existent_full_update():
    """
    Testing API response when sending a PUT request for an invalid ID
    """
    random_id = random.randint(900000000000000, 1000000000000000)
    put_response = full_update(str(random_id), create_payload())
    assert put_response.status_code == 404
    assert "error" in put_response.json()


@pytest.mark.negative
def test_non_existent_partial_update():
    """
        Testing API response when sending a PATCH request for an invalid ID
        """
    random_id = random.randint(90000000000000, 100000000000000)
    payload = {
        "name": "Testing invalid patch response"
    }
    patch_response = partial_update(str(random_id), payload)
    assert patch_response.status_code == 404
    assert "error" in patch_response.json()


@pytest.mark.negative
def test_invalid_content_type():
    """
    Testing API response when sending a PUT request for an unsupported content type using header
    """
    rand_id = random.randint(1, 10)  # we know that server already has id's from 1 to 10
    put_response = full_update_with_header(str(rand_id), create_payload())
    assert put_response.status_code in range(400, 500)
    assert "error" in put_response.json()
