
import os

from pkg_resources import resource_filename
from spyne.interface.xml_schema.parser import Thier_repr
from spyne.util.xml import parse_schema_file

_common = lambda f: os.path.abspath(resource_filename(__name__ + '.common', f))
_maindoc = lambda f: os.path.abspath(resource_filename(__name__ + '.maindoc', f))
_root = lambda f: os.path.abspath(resource_filename(__name__, f))


class NS:
    QDT = 'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2'
    IMMT = 'urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003'
    UDTSM = 'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2'
    XADES = 'http://uri.etsi.org/01903/v1.3.2#'
    CL_5639 = 'urn:un:unece:uncefact:codelist:specification:5639:1988'
    UBLTR_INV = 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2'
    UBL_CAC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
    UBL_CBC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    UBL_CEC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'
    XMLDSIG = 'http://www.w3.org/2000/09/xmldsig#'
    XMLMIME = 'http://www.w3.org/2005/05/xmlmime'
    UBLTR_AR = 'urn:oasis:names:specification:ubl:schema:xsd:ApplicationResponse-2'
    CL_54217 = 'urn:un:unece:uncefact:codelist:specification:54217:2001'
    CL_66411 = 'urn:un:unece:uncefact:codelist:specification:66411:2001'


files = {
    NS.UBL_CAC: _common('UBL-CommonAggregateComponents-2.0.xsd'),
    NS.UBL_CBC: _common('UBL-CommonBasicComponents-2.0.xsd'),

    u'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2':
        _common('UnqualifiedDataTypeSchemaModule-2.0.xsd'),

    u'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2':
        _common('UBL-QualifiedDatatypes-2.0.xsd'),

    u'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2':
        _common('UBL-CommonExtensionComponents-2.0.xsd'),

    u'urn:un:unece:uncefact:codelist:specification:66411:2001':
        _common('CodeList_UnitCode_UNECE_7_04.xsd'),

    u'urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003':
        _common('CodeList_MIMEMediaTypeCode_IANA_7_04.xsd'),

    u"urn:un:unece:uncefact:codelist:specification:54217:2001":
        _common('CodeList_CurrencyCode_ISO_7_04.xsd'),

    u"urn:un:unece:uncefact:codelist:specification:5639:1988":
        _common('CodeList_LanguageCode_ISO_7_04.xsd'),
    u"http://www.w3.org/2000/09/xmldsig#":
        _common('xmldsig-core-schema.xsd'),
    u"http://uri.etsi.org/01903/v1.3.2#":
        _common('XAdES.xsd'),

    NS.UBLTR_AR: _maindoc('UBLTR-ApplicationResponse-2.0.xsd'),
    NS.UBLTR_INV: _maindoc('UBLTR-Invoice-2.0.xsd'),
    NS.XMLMIME: _root('xmlmime.xsd')
}


ns_mapper = lambda ns, name: '%s.%s' % ({
    'http://uri.etsi.org/01903/v1.3.2#': "xades",
    'http://www.w3.org/2005/05/xmlmime': "xmlmime",
    'http://www.w3.org/2000/09/xmldsig#': "xmldsig",
    'urn:un:unece:uncefact:codelist:specification:5639:1988': "cl5639",
    'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2': "inv",
    'urn:un:unece:uncefact:codelist:specification:54217:2001': "cl54217",
    'urn:un:unece:uncefact:codelist:specification:66411:2001': "cl66411",
    'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2': "qdt",
    'urn:oasis:names:specification:ubl:schema:xsd:ApplicationResponse-2': "ar",
    'urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003': "immt",
    'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2': "cbc",
    'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2': "cac",
    'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2': "cec",
    'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2': "udtsm",
}[ns], name)

_ns_mapper = lambda ns, name:"UBLTR_APP_RESPONSE[%s].types[%r]" % ({
    'http://uri.etsi.org/01903/v1.3.2#': "NS.XADES",
    'http://www.w3.org/2005/05/xmlmime': "NS.XMLMIME",
    'http://www.w3.org/2000/09/xmldsig#': "NS.XMLDSIG",
    'urn:un:unece:uncefact:codelist:specification:5639:1988': "NS.CL_5639",
    'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2': "NS.UBLTR_INV",
    'urn:un:unece:uncefact:codelist:specification:54217:2001': "NS.CL_54217",
    'urn:un:unece:uncefact:codelist:specification:66411:2001': "NS.CL_66411",
    'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2': "NS.QDT",
    'urn:oasis:names:specification:ubl:schema:xsd:ApplicationResponse-2': "NS.UBLTR_AR",
    'urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003': "NS.IMMT",
    'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2': "NS.UBL_CBC",
    'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2': "NS.UBL_CAC",
    'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2': "NS.UBL_CEC",
    'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2': "NS.UDTSM",
}[ns], name)

# comment these out for production
import sys
sys.stdout.write('# parsing schemas...')
sys.stdout.flush()
import logging
logging.basicConfig(level=logging.DEBUG)

XMLMIME_SCHEMA = parse_schema_file(files[NS.XMLMIME])
UBLTR_APP_RESPONSE = parse_schema_file(files[NS.UBLTR_AR], files, repr_=Thier_repr(with_ns=ns_mapper))
UBLTR_INVOICE = parse_schema_file(files[NS.UBLTR_INV], files, repr_=Thier_repr(with_ns=ns_mapper))

# and these
sys.stdout.write(' done.\n')
sys.stdout.flush()
