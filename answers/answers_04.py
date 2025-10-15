import requests
import pytest


# Exercise 4.1
# Create a new GraphQL query as a String with value { company { name ceo coo } }
# POST this object to https://spacex-production.up.railway.app/
# Assert that the name of the CEO is Elon Musk
# The name can be found using ['data']['company']['ceo']
def test_get_company_data_check_ceo_should_be_elon_musk():

    response = requests.post(
        'https://spacex-production.up.railway.app/',
        json={'query': '{ company { name ceo coo } }'}
    )
    response_body = response.json()
    assert response_body['data']['company']['ceo'] == 'Elon Musk'


# Exercise 4.2
# Create a test data source (a list of test data tuples)
# containing the following test data:
# --------------------------------------------------------------------------
# rocket id                | rocket name  | country
# --------------------------------------------------------------------------
# 5e9d0d95eda69955f709d1eb | Falcon 1     | Republic of the Marshall Islands
# 5e9d0d95eda69974db09d1ed | Falcon Heavy | United States
# 5e9d0d96eda699382d09d1ee | Starship     | United States
test_data_rockets = [
    ('5e9d0d95eda69955f709d1eb', 'Falcon 1', 'Republic of the Marshall Islands'),
    ('5e9d0d95eda69974db09d1ed', 'Falcon Heavy', 'United States'),
    ('5e9d0d96eda699382d09d1ee', 'Starship', 'United States')
]


# Exercise 4.3
# Write a test that POSTs the given parameterized GraphQL query to
# https://spacex-production.up.railway.app/, together with the rocket id as
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
        'https://spacex-production.up.railway.app/',
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
