import requests
import uuid

unique_number = str(uuid.uuid4())  # e.g. 5b4832b4-da4c-48b2-8512-68fb49b69de1


def create_json_object():

    return {
        "users": [
            {
                "user": {
                    "id": unique_number,
                    "name": "John Smith",
                    "phone_1": "0612345678",
                    "phone_2": "0992345678",
                }
            }
        ]
    }


def test_send_json_with_unique_number_check_status_code():
    response = requests.post("http://httpbin.org/post", json=create_json_object())
    print(response.request.body)
    assert response.status_code == 200
