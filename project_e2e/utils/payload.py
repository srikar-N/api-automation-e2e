import random


def create_payload():
    """
    Create a dynamic payload with random values.
    """
    return {
        "name": f"Apple MacBook Pro {random.randint(1, 10)}",
        "data": {
            "year": random.randint(2015, 2024),
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }


def create_empty_payload():
    """
    Create an empty data payload.
    """
    return {
        "name": "Apple MacBook Pro",
        "data": {}
    }
