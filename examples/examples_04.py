from lxml import etree

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

    return '''
    <users>
        <user>
            <id>5b4832b4-da4c-48b2-8512-68fb49b69de1</id>
            <name>John Smith</name>
            <phone type="mobile">0612345678</phone>
            <phone type="landline">0992345678</phone>
        </user>
    </users>    
    '''


def create_xml_object():
    users = etree.Element("users")
    user = etree.SubElement(users, "user")
    user_id = etree.SubElement(user, "id")
    user_id.text = unique_number
    name = etree.SubElement(user, "name")
    name.text = "John Smith"
    phone1 = etree.SubElement(user, "phone")
    phone1.set("type", "mobile")
    phone1.text = "0612345678"
    phone2 = etree.SubElement(user, "phone")
    phone2.set("type", "landline")
    phone2.text = "0992345678"

    return users


def test_send_xml_using_xml_string_block():
    response = requests.post("http://httpbin.org/anything", data=use_xml_string_block())
    print(response.request.body)
    assert response.status_code == 200


def test_send_xml_using_lxml_etree():
    xml = create_xml_object()
    response = requests.post("http://httpbin.org/anything", data=etree.tostring(xml))
    print(response.request.body)
    assert response.status_code == 200
