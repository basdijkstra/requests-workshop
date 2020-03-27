import xml.etree.ElementTree as et
import requests


# Exercise 5.1
# Write a test that does the following:
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Check that the root element name is 'account'
# Check that the root element has no attributes
# Check that the root element has no text
def test_check_root_of_xml_response():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/accounts/12345"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    root = xml_tree.getroot()
    assert root.tag == "account"
    assert len(root.attrib) == 0
    assert root.text is None


# Exercise 5.2
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Find the customerId element in the tree
# Check that the text of the customerId element is '12212'
def test_check_specific_element_of_xml_response():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/accounts/12345"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    first_name = xml_tree.find("customerId")
    assert first_name.text == "12212"


# Exercise 5.3
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts
# Parse the response into an XML ElementTree
# Find all 'account' elements in the entire XML document
# Check that there are more than 5 of these 'account' elements
def test_check_number_of_accounts_for_12212_greater_than_five():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    accounts = xml_tree.findall(".//account")
    assert len(accounts) > 5


# Exercise 5.4
# Repeat Exercise 5.3, but now check that:
# - at least one of the accounts is of type 'SAVINGS' (Google!)
# - there is no account that has a customerId that is not equal to 12212
#   (Use your creativity with the last one here... There is a solution, but I couldn't
#    find it on Google.)
def test_use_xpath_for_more_sophisticated_checks():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    savings_accounts = xml_tree.findall(".//account/type[.='SAVINGS']")
    assert len(savings_accounts) > 1
    accounts_with_incorrect_customer_id = xml_tree.findall(
        ".//account/customerId[!.='12212']"
    )
    assert len(accounts_with_incorrect_customer_id) == 0
