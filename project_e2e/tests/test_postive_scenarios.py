from datetime import datetime

import pytest

from project_e2e.Api.objects import bulk_get, get_data_by_ids, get_data


@pytest.mark.positive
def test_bulk_get():
    """
    Testing API response when sending a Bulk Get request
    """
    bulk_response = bulk_get()
    assert bulk_response.status_code == 200
    assert len(bulk_response.json()) > 0


@pytest.mark.positive
def test_get_data_with_id(create_two_objects):
    """
        Testing API response when sending a Get request with Multiple ids
    """
    object_id_1, object_id_2 = create_two_objects
    multi_id_response = get_data_by_ids(object_id_1, object_id_2)
    assert multi_id_response.status_code == 200
    assert len(multi_id_response.json()) == 2
    assert multi_id_response.json()[0]["id"] == object_id_1
    assert multi_id_response.json()[1]["id"] == object_id_2


@pytest.mark.positive
def test_schema_validation(send_post_response):
    """
        Testing API response when sending POST request and validating Data types in response
    """
    object_response = send_post_response
    assert isinstance(object_response["id"], str)
    assert isinstance(object_response["data"], dict)
    assert isinstance(object_response["data"]["year"], int)
    assert isinstance(object_response["data"]["price"], float)
    assert isinstance(object_response["data"]["CPU model"], str)
    assert isinstance(object_response["data"]["Hard disk size"], str)
    assert "createdAt" in object_response
    timestamp = object_response["createdAt"]
    parsed_time = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    assert isinstance(parsed_time, datetime)


@pytest.mark.positive
def test_empty_data_payload(create_empty_object):
    """
        Testing API response when sending empty data payload.
    """
    object_id, payload = create_empty_object
    get_response = get_data(object_id)
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == object_id
    del data["id"]
    assert data["data"] == {}
    assert data["name"] == "Apple MacBook Pro"
