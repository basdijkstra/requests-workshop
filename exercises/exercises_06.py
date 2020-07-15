import requests
import responses
import pytest
import json

from urllib.parse import urlparse


# Exercise 6.1
# Write a test that does the following:
# Create a mock that returns an HTTP status code 404
#   for a GET request to http://api.zippopotam.us/us/90210
# Perform a GET to http://api.zippopotam.us/us/90210
# Check that the status code is indeed equal to 404


# Exercise 6.2
# Write a test that does the following:
# Create a mock that returns an HTTP status code 404
#   for a GET request to http://api.zippopotam.us/us/90210
#   as well as a JSON response body that looks like this:
#   {'error': 'No data exists for US zip code 90210'}
# Perform a GET to http://api.zippopotam.us/us/90210
# Check that the value of the 'error' element in the JSON
# response is indeed equal to 'No data exists for US zip code 90210'


# Exercise 6.3
# Write a test that does the following:
# Create a mock that raises a ValueError
#   for a GET request to http://api.zippopotam.us/us/ABCDE
#   with a message 'US uses numerical zip codes only'
# Perform a GET to http://api.zippopotam.us/us/ABCDE
# Check that a ValueError is raised indeed and that the
#   associated message equals 'US uses numerical zip codes only'


# Exercise 6.4
# Create a test data object test_data_zip
# with three lines / test cases:
# country code - zip code - place
#           us -    90210 - Beverly Hills
#           it -    50123 - Firenze
#           ca -      Y1A - Whitehorse
# (this is the same data source as used in Exercise 2.1)


# Exercise 6.5
# Create a mock that uses a callback to create dynamic responses
# Upon receiving a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
#   it should return a status code 200 and a JSON response body like this:
#   {'value': '<country_code> zip code <zip_code> corresponds to <place>'}
# Create a parameterized test (see Exercise 2.2) that takes three
#   arguments: country_code and zip_code as input parameters and place as
#   expected output. Perform a GET call to http://api.zippopotam.us/<country_code>/<zip_code>
#   and check that the response body element 'value' has a value equal to
#   '<country_code> zip code <zip_code> corresponds to <place>'.
