import xml.etree.ElementTree as et
import requests


def test_check_root_of_xml_response():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/customers/12212"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    root = xml_tree.getroot()
    assert root.tag == "customer"
    assert root.text is None


def test_check_specific_element_of_xml_response():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/customers/12212"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    first_name = xml_tree.find("firstName")
    assert first_name.text == "John"
    assert len(first_name.attrib) == 0


# https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath
def test_use_xpath_for_more_sophisticated_checks():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/customers/12212"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    address_children = xml_tree.findall(".//address/*")
    assert len(address_children) == 4
