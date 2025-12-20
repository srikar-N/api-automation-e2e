import requests

End_point = "https://api.restful-api.dev/objects"


def send_data(payload):
    """
    Send a POST request to the API endpoint with the given payload.
    """
    response = requests.post(End_point, json=payload)
    return response


def get_data(object_id):
    """
    Send a GET request to the API endpoint with the given object ID.
    """
    response = requests.get(End_point + "/" + object_id)
    return response


def full_update(obj_id, payload):
    """
    Send a PUT request to the API endpoint with the given object ID and payload.
    """
    update_response = requests.put(End_point + "/" + obj_id, json=payload)
    return update_response


def partial_update(obj_id, patched_payload):
    """
    Send a PATCH request to the API endpoint with the given object ID and patched payload.
    """
    patch_response = requests.patch(End_point + "/" + obj_id, json=patched_payload)
    return patch_response


def delete_data(obj_id):
    """
    Send a DELETE request to the API endpoint with the given object ID.
    """
    delete_response = requests.delete(End_point + "/" + obj_id)
    return delete_response


def bulk_get():
    """
    Send a GET request to the API endpoint to retrieve all objects.
    """
    response = requests.get(End_point)
    return response


def get_data_by_ids(*args):
    """
    Send a GET request to the API endpoint with the given object IDs.
    """
    if len(args) == 1:
        resource = End_point + f"?id={args[0]}"
    else:
        resource = End_point + f"?id={args[0]}"
        for obj_id in range(1, len(args)):
            resource = resource + "&id=" + args[obj_id]

    response = requests.get(resource)
    return response


def send_invalid_json(payload):
    """
    Send a POST request to the API endpoint with an invalid JSON payload.
    """
    header = {
        "Content-Type": "application/json"
    }
    response = requests.post(End_point, data=payload, headers=header)
    return response


def full_update_with_header(object_id, payload):
    """
    Update request with header.
    """
    header = {
        "Content-Type": "text/plain"
    }
    update_response = requests.put(End_point + "/" + object_id, headers=header, data=payload)
    return update_response
