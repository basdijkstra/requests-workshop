import pytest, requests, csv

# Exercise 2.1
# Create a test data object test_data_zip
# with three lines / test cases:
# country code - zip code - place
#           us -    90210 - Beverly Hills
#           it -    50123 - Firenze
#           ca -      Y1A - Whitehorse
test_data_zip = [
    ("us", "90210", "Beverly Hills"),
    ("it", "50123", "Firenze"),
    ("ca", "Y1A", "Whitehorse"),
]


# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
# and checks that the values for the 'place name' elements correspond
# to those that are specified in the test data object
@pytest.mark.parametrize("country_code, zip_code, expected_place", test_data_zip)
def test_get_location_data_check_place_name(country_code, zip_code, expected_place):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place


# Exercise 2.3
# Create the same test data as above, but now in a .csv file, for example:
# us,90210,Beverly Hills
# it,50123,Firenze
# ca,Y1A,Whitehorse
# Place this .csv file in the answers folder of the project


# Exercise 2.4
# Create a method read_data_from_csv() that reads the file from 2.3 line by line
# and creates and returns a test data object from the data in the .csv file
def read_data_from_csv():
    test_data_zip_from_csv = []
    with open("answers/test_data_zip.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        for row in data:
            test_data_zip_from_csv.append(row)
    return test_data_zip_from_csv


# Exercise 2.5
# Change the data driven test from Exercise 2.2 so that it uses the test data
# from the .csv file instead of the test data that was hard coded in this file
@pytest.mark.parametrize("country_code, zip_code, expected_place", read_data_from_csv())
def test_get_location_data_check_place_name_with_data_from_csv(
    country_code, zip_code, expected_place
):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place
