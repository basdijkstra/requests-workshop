import xml.etree.ElementTree as et
import requests


# Exercise 5.1
# Write a test that does the following:
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Check that the root element name is 'account'
# Check that the root element has no attributes
# Check that the root element has no text


# Exercise 5.2
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Find the customerId element in the tree
# Check that the text of the customerId element is '12212'


# Exercise 5.3
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts
# Parse the response into an XML ElementTree
# Find all 'account' elements in the entire XML document
# Check that there are more than 5 of these 'account' elements


# Exercise 5.4
# Repeat Exercise 5.3, but now check that:
# - at least one of the accounts is of type 'SAVINGS' (Google!)
# - there is no account that has a customerId that is not equal to 12212
#   (Use your creativity with the last one here... There is a solution, but I couldn't
#    find it on Google.)
