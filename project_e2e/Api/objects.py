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
    response = requests.get(End_point+"/"+object_id)
    return response

def full_update(obj_id,payload):
    """
    Send a PUT request to the API endpoint with the given object ID and payload.
    """
    update_response = requests.put(End_point +"/"+obj_id, json=payload)
    return update_response


def partial_update(obj_id,patched_payload):
    """
    Send a PATCH request to the API endpoint with the given object ID and patched payload.
    """
    patch_response = requests.patch(End_point+"/"+obj_id, json=patched_payload)
    return patch_response

def delete_data(obj_id):
    """
    Send a DELETE request to the API endpoint with the given object ID.
    """
    delete_response = requests.delete(End_point+"/"+obj_id)
    return delete_response