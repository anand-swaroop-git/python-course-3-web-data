# The act of going from an internal representation on one computer out to a sort of interchange format is called serialization. And that has to do with the fact that, in the old days we had these wires, and we sent the data serially, across one character at a time. So it was taking, from the internal memory of the computer a format that we could sort of send one character at a time, character, character, character, character, character, so we called this a serialization format.
# The act of taking the data off of the wire and turning it into a new internal data structure, in the new environment, potentially in a very new language, is called de-serialization. So we take our internal structure, serialize it, send it across the network, then we receive it. We de-serialize it, and then we use it in this other programming language, in whatever structure makes sense, in that particular programming language. 
# The two types of serialization formats that we're going to talk about are XML and JSON. And so those are the two. And XML's kind of like the older of the two, and JSON is the more modern of the two. XML is the more complex and, some would say, more rigorous of the two, and JSON is the lighter-weight version of it.

# Xtensible Markup Language
# XML Elements or Nodes
# <people>​
#     <person>​
#     #Simple Elements since the tags just contain some plain text/number
#        <name>Chuck</name>​
#        <phone>303 4456</phone>​
#     </person>​
#     #Complex Elements since the tags contain child tags
#     <person>​
#        <name>Noah</name>​
#        <phone>622 7421</phone>​
#     </person>​
# </people>​

# Primary purpose is to help information systems share structured data​
# It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible​

# XML Basics
# Sample XML Code:
# <person>​
#   <name>Chuck</name>​
#   <phone type="intl">​
#      +1 734 303 4456​
#    </phone>​
#    <email hide="yes" />​
# </person>​

# In the above XML code, following are the examples of XML elements
# Start Tag​         |     <person>​
# End Tag​           |     </person>​
# Text Content​      |     Chuck, +1 734 303 4456​
# Attribute​         |     type="intl" , hide="yes" (Key-Value pair on the opening tag of XML)
# Self Closing Tag  |     <email hide="yes" />​

# XML Schema
# Description of the legal format of an XML document​
# Expressed in terms of constraints on the structure and content of documents​
# Often used to specify a “contract” between systems - “My system will only accept XML that conforms to this particular Schema.”​
# If a particular piece of XML meets the specification of the Schema - it is said to “validate”​
#  XML validation is the act of taking an document and a Schema Contract, which itself is also an XML document, and then sending to the Validator. 

# XML Document
# <person>​
#    <lastname>Severance</lastname>​
#    <age>17</age>​
#    <dateborn>2001-04-17</dateborn>​
# </person>

# XML Schema Contract​ for validating the above XML document
# <xs:complexType name=”person”>​
#   <xs:sequence>​
#     <xs:element name="lastname" type="xs:string"/>​
#     <xs:element name="age" type="xs:integer"/>​
#     <xs:element name="dateborn" type="xs:date"/>​
#    </xs:sequence>​
# </xs:complexType

# Many XML Schema Languages​
# Document Type Definition (DTD)​
# -  http://en.wikipedia.org/wiki/Document_Type_Definition​
# Standard Generalized Markup Language (ISO 8879:1986 SGML)​
# -  http://en.wikipedia.org/wiki/SGML​
# XML Schema  from W3C - (XSD)​
# -  http://en.wikipedia.org/wiki/XML_Schema_(W3C)​

# XSD XML Schema (W3C spec)​
# We will focus on the World Wide Web Consortium (W3C) version​
# It is often called “W3C Schema” because “Schema” is considered generic​
# More commonly it is called XSD because the file names end in .xsd​

# XSD examples
# <xs:element name="person">​
#   <xs:complexType>​
#     <xs:sequence>​
#       <xs:element name="full_name" type="xs:string"  ​
#           minOccurs="1" maxOccurs="1" />​
#       <xs:element name="child_name" type="xs:string" ​
#             minOccurs="0" maxOccurs="10" />​
#     </xs:sequence>​
#   </xs:complexType>​
# </xs:element>​
    # Valid XML for the above XSD
    # <person>​
    # <full_name>Tove Refsnes</full_name>​
    # <child_name>Hege</child_name>​
    # <child_name>Stale</child_name>​
    # <child_name>Jim</child_name>​
    # <child_name>Borge</child_name>​
    # </person>

# XSD example #2
# <xs:element name="customer" type="xs:string"/>​
# <xs:element name="start" type="xs:date"/>​
# <xs:element name="startdate" type="xs:dateTime"/>​
# <xs:element name="prize" type="xs:decimal"/>​
# <xs:element name="weeks" type="xs:integer"/>​
    # Valid XML for the above XSD
    # <customer>John Smith</customer>​
    # <start>2002-09-24</start>​
    # <startdate>2002-05-30T09:30:10Z</startdate>​
    # <prize>999.50</prize>​
    # <weeks>30</weeks>​

# ISO 8601 Date/Time format
# http://en.wikipedia.org/wiki/Coordinated_Universal_Time​
# http://en.wikipedia.org/wiki/ISO_8601​ 
# 2002-05-30T09:30:10Z​
# In the above, Z => Timezone - typically specified in UTC / GMT rather than local time zone​


# Parsing XML with Python
# import xml.etree.ElementTree as ET
# data = '''
# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#      +1 734 303 4456
#    </phone>
#    <email hide="yes"/>
# </person>'''

# tree = ET.fromstring(data)
# print 'Name:',tree.find('name').text
# print 'Attr:',tree.find('email').get('hide')


# Parsing XML with Python - Second Example
# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#             </user>
#         </users>
# </stuff>'''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print 'User count:', len(lst)
# for item in lst:
#     print 'Name', item.find('name').text
#     print 'Id', item.find('id').text
#     print 'Attribute', item.get("x")

# Assignment of week 5 - Extracting Data from XML
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# # extract all the comment/count values from the url and get the sum of all of them
# url = 'http://py4e-data.dr-chuck.net/comments_133481.xml'
# # get the content of the url as a string
# data = urllib.request.urlopen(url).read()
# # transform the string content into a xml tree
# tree = ET.fromstring(data)
# # find all count elements
# counts = tree.findall('comments/comment/count')
# # extract the value of each count element and add it to the total
# total = 0
# for count in counts:
#     total += int(count.text)
# print('total: ', total)