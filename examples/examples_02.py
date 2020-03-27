import pytest
import requests
import csv

test_data_users = [(1, "Leanne Graham"), (2, "Ervin Howell"), (3, "Clementine Bauch")]


@pytest.mark.parametrize("userid, expected_name", test_data_users)
def test_get_data_for_user_check_name(userid, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    response_body = response.json()
    assert response_body["name"] == expected_name


def read_data_from_csv():
    test_data_users_from_csv = []
    with open("examples/test_data_users.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        for row in data:
            test_data_users_from_csv.append(row)
    return test_data_users_from_csv


@pytest.mark.parametrize("userid, expected_name", read_data_from_csv())
def test_get_location_data_check_place_name_with_data_from_csv(userid, expected_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userid}")
    response_body = response.json()
    assert response_body["name"] == expected_name
