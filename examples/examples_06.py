import requests
import pytest

query_weather_in_amsterdam = """
{
  getCityByName(name: "Amsterdam") {
    weather {
      summary {
        title
      }
    }
  }
}
"""


def test_get_weather_for_amsterdam_should_be_clear():
    response = requests.post(
        "https://graphql-weather-api.herokuapp.com/",
        json={'query': query_weather_in_amsterdam}
    )
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['data']['getCityByName']['weather']['summary']['title'] == 'Clear'


query_weather_parameterized = """
query getWeather($city: String!)
{
  getCityByName(name: $city) {
    weather {
      summary {
        title
      }
    }
  }
}
"""

test_data_weather = [
    ('Amsterdam', 'Clear'),
    ('Berlin', 'Clear'),
    ('Sydney', 'Rain')
]


@pytest.mark.parametrize('city_name, expected_weather', test_data_weather)
def test_get_weather_for_city_should_be_as_expected(city_name, expected_weather):
    response = requests.post(
        "https://graphql-weather-api.herokuapp.com/",
        json={'query': query_weather_parameterized,
              'variables': {
                  'city': city_name
              }}
    )
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['data']['getCityByName']['weather']['summary']['title'] == expected_weather
