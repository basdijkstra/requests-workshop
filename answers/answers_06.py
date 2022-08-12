import requests
import pytest


# Exercise 6.1
# Create a new GraphQL query as a String with value { company { name ceo coo } }
# POST this object to https://api.spacex.land/graphql/
# Assert that the name of the CEO is Elon Musk
# The name can be found using ['data']['company']['ceo']
def test_get_company_data_check_ceo_should_be_elon_musk():

    response = requests.post(
        'https://api.spacex.land/graphql/',
        json={'query': '{ company { name ceo coo } }'}
    )
    response_body = response.json()
    assert response_body['data']['company']['ceo'] == 'Elon Musk'


# Exercise 6.2
# Create a test data source (a list of test data tuples)
# containing the following test data:
# ------------------------------------
# rocket id   | rocket name  | country
# ------------------------------------
# falcon1     | Falcon 1     | Republic of the Marshall Islands
# falconheavy | Falcon Heavy | United States
# starship    | Starship     | United States
test_data_rockets = [
    ('falcon1', 'Falcon 1', 'Republic of the Marshall Islands'),
    ('falconheavy', 'Falcon Heavy', 'United States'),
    ('starship', 'Starship', 'United States')
]


# Exercise 6.3
# Write a test that POSTs the given parameterized GraphQL query to
# https://api.spacex.land/graphql, together with the rocket id as
# the value for the id variable, for all test cases in the test data source.
#
# Assert that the name of the rocket is equal to the value in the data source
# Use ['data']['rocket']['name'] to extract it from the JSON response body.
#
# Assert that the country where the rocket was launched is equal to the value in the data source
# Use ['data']['rocket']['country'] to extract it from the JSON response body.
query_rocket_parameterized = """
query getRocketData($id: ID!)
{
  rocket(id: $id) {
    name
    country
  }
}
"""


@pytest.mark.parametrize('rocket_id, rocket_name, country', test_data_rockets)
def test_get_rocket_data_check_name_and_country_should_equal_expected(rocket_id, rocket_name, country):

    response = requests.post(
        'https://api.spacex.land/graphql/',
        json={
            'query': query_rocket_parameterized,
            'variables': {
                'id': rocket_id
            }
        }
    )
    response_body = response.json()
    assert response_body['data']['rocket']['name'] == rocket_name
    assert response_body['data']['rocket']['country'] == country
