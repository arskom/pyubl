#!/usr/bin/env python3

from ubl.const.schema.parsed import xmldsig
from ubl.const.schema.parsed import NS
from spyne.interface.xml_schema import parser
from spyne.util.xml import get_xml_as_object
from spyne.util.xml import get_object_as_xml

from lxml import etree


data = open('example.xml', 'r').read()
data_elt = etree.fromstring(data, parser=parser.PARSER)
sig_elt = data_elt.xpath('ds:Signature', namespaces={'ds': NS.XMLDSIG})[0];
print get_xml_as_object(sig_elt, xmldsig.SignatureType)
