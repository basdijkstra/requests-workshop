import requests
import responses
import pytest
import json

from urllib.parse import urlparse
from requests.exceptions import ConnectionError


@responses.activate
def test_get_user_with_id_1_mock_returns_404():

    responses.add(
        responses.GET, "https://jsonplaceholder.typicode.com/users/1", status=404
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 404


@responses.activate
def test_get_user_with_id_1_mock_returns_404_and_error_message_in_body():

    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/users/1",
        json={"error": "No data exists for user with ID 1"},
        status=404,
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.json()["error"] == "No data exists for user with ID 1"


@responses.activate
def test_unmatched_endpoint_raises_connectionerror():

    with pytest.raises(ConnectionError):
        requests.get("https://jsonplaceholder.typicode.com/users/99")


@responses.activate
def test_responses_can_raise_error_on_demand():

    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/users/99",
        body=RuntimeError("A runtime error occurred"),
    )

    with pytest.raises(RuntimeError) as re:
        requests.get("https://jsonplaceholder.typicode.com/users/99")
    assert str(re.value) == "A runtime error occurred"


test_data = [1, 2, 3]


@pytest.mark.parametrize("userid", test_data)
@responses.activate
def test_using_a_callback_for_dynamic_responses(userid):
    def request_callback(request):
        request_url = request.url
        resp_body = {"value": generate_response_from(request_url)}
        return 200, {}, json.dumps(resp_body)

    responses.add_callback(
        responses.GET,
        f"https://jsonplaceholder.typicode.com/users/{userid}",
        callback=request_callback,
        content_type="application/json",
    )

    def generate_response_from(url):
        parsed_url = urlparse(url).path
        split_url = parsed_url.split("/")
        return f"You requested data for user {split_url[-1]}"

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    assert response.json()["value"] == f"You requested data for user {userid}"
