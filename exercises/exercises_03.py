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
