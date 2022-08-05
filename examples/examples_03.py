import requests
import random


def create_new_post_object():

    return {
        "name": "John Smith",
        "address": {
            "street": "Main Street",
            "number": random.randint(1000, 9999),
            "zipCode": 90210,
            "city": "Beverly Hills"
        }
    }


def test_send_json_with_unique_number_check_status_code():
    response = requests.post("https://postman-echo.com/post", json=create_new_post_object())
    print(response.request.body)
    assert response.status_code == 200
