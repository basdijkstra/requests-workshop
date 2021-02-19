import requests


# Exercise 3.1
# Create a function create_post() that returns an
# object that follows this structure:
# {
#     "title": "The title of my new post",
#     "body": "A very long string containing the body of my new post",
#     "userId": 1
# }


# Exercise 3.2
# Write a test that POSTs the object created in 3.1
# as JSON to https://jsonplaceholder.typicode.com/posts
# and checks that the response status code is 201
# and that the new post id returned by the API is an integer
# Use the isinstance(variable, type) function for this (Google is your friend!)


# Exercise 3.3
# Create a function create_billpay_for(name) that takes
# an argument of type string containing a name and returns
# an object that follows this structure:
# {
#   "name": <value of the name>,
#   "address": {
#     "street": "My street",
#     "city": "My city",
#     "state": "My state",
#     "zipCode": "90210"
#   },
#   "phoneNumber": "0123456789",
#   "accountNumber": 12345
# }


# Exercise 3.4
# Write a test that POSTs the object created in 3.3 to
# https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500
# Supply a name of your own choice to the create_billpay_for() method
# Make sure that the request header 'Accept' has value 'application/json' (Google ;)
# Check that the response status code is 200 and
# that the response body element 'payeeName' equals the name supplied to the method
