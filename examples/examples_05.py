from lxml import etree

import requests


def test_check_root_of_xml_response():
    response = requests.get(
        "https://parabank.parasoft.com/parabank/services/bank/customers/12212"
    )
    xml_response_element = etree.fromstring(response.content)
    xml_response_tree = etree.ElementTree(xml_response_element)
    root = xml_response_tree.getroot()
    assert root.tag == "customer"
    assert root.text is None


def test_check_specific_element_of_xml_response():
    response = requests.get(
        "https://parabank.parasoft.com/parabank/services/bank/customers/12212"
    )
    xml_response_element = etree.fromstring(response.content)
    xml_response_tree = etree.ElementTree(xml_response_element)
    first_name = xml_response_tree.find("firstName")
    assert first_name.text == "John"
    assert len(first_name.attrib) == 0


# https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath
def test_use_xpath_for_more_sophisticated_checks():
    response = requests.get(
        "https://parabank.parasoft.com/parabank/services/bank/customers/12212"
    )
    xml_response_element = etree.fromstring(response.content)
    xml_response_tree = etree.ElementTree(xml_response_element)
    address_children = xml_response_tree.findall(".//address/*")
    assert len(address_children) == 4
