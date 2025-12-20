import pytest

from project_e2e.Api.objects import bulk_get, get_data


@pytest.mark.misc
def test_response_time():
    bulk_get_response = bulk_get()
    assert bulk_get_response.status_code == 200
    assert bulk_get_response.elapsed.total_seconds() < 1


@pytest.mark.misc
def test_data_integrity(send_post_response):
    object_id = send_post_response["id"]
    response = get_data(object_id)
    assert response.status_code == 200
    get_response = response.json()
    assert isinstance(get_response["id"], str)
    assert isinstance(get_response["data"], dict)
    assert isinstance(get_response["data"]["year"], int)
    assert isinstance(get_response["data"]["price"], float)
    assert isinstance(get_response["data"]["CPU model"], str)
    assert isinstance(get_response["data"]["Hard disk size"], str)
    assert isinstance(get_response["data"]["Is Available"], bool)
