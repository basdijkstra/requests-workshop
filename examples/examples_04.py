import xml.etree.ElementTree as et
import requests
import uuid

unique_number = str(uuid.uuid4())

# <users>
# 	<user>
# 		<id>5b4832b4-da4c-48b2-8512-68fb49b69de1</id>
# 		<name>John Smith</name>
# 		<phone type="mobile">0612345678</phone>
# 		<phone type="landline">0992345678</phone>
# 	</user>
# </users>


def use_xml_string_block():

    return """
    <users>
        <user>
            <id>5b4832b4-da4c-48b2-8512-68fb49b69de1</id>
            <name>John Smith</name>
            <phone type="mobile">0612345678</phone>
            <phone type="landline">0992345678</phone>
        </user>
    </users>    
    """


def create_xml_object():
    users = et.Element("users")
    user = et.SubElement(users, "user")
    user_id = et.SubElement(user, "id")
    user_id.text = unique_number
    name = et.SubElement(user, "name")
    name.text = "John Smith"
    phone1 = et.SubElement(user, "phone")
    phone1.set("type", "mobile")
    phone1.text = "0612345678"
    phone2 = et.SubElement(user, "phone")
    phone2.set("type", "landline")
    phone2.text = "0992345678"

    return users


def test_send_xml_using_xml_string_block():
    xml = use_xml_string_block()
    response = requests.post("http://httpbin.org/anything", data=xml)
    print(response.request.body)
    assert response.status_code == 200


def test_send_xml_using_element_tree():
    xml = create_xml_object()
    xml_as_string = et.tostring(xml)
    response = requests.post("http://httpbin.org/anything", data=xml_as_string)
    print(response.request.body)
    assert response.status_code == 200
