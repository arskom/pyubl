# encoding: utf8
#
# Copyright (c), Arskom Ltd. and pyubl contributors, see CONTRIBUTORS file.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#
# * Neither the name of pyubl nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


from ubl.const.schema import NS
from ubl.const.schema import UBLTR_APP_RESPONSE
from ubl.const.schema import UBLTR_INVOICE



class inv:
    InvoiceType = UBLTR_INVOICE[NS.UBLTR_INV].types['InvoiceType']


class ar:
    ApplicationResponseType = UBLTR_APP_RESPONSE[NS.UBLTR_AR].types[u'ApplicationResponseType']


class cac:
    AddressType = UBLTR_APP_RESPONSE[NS.UBL_CAC].types[u'AddressType']
    AttachmentType = UBLTR_INVOICE[NS.UBL_CAC].types['AttachmentType']
    ContactType = UBLTR_INVOICE[NS.UBL_CAC].types['ContactType']
    CountryType = UBLTR_INVOICE[NS.UBL_CAC].types['CountryType']
    CustomerPartyType = UBLTR_INVOICE[NS.UBL_CAC].types['CustomerPartyType']
    DocumentResponseType = UBLTR_INVOICE[NS.UBL_CAC].types['DocumentResponseType']
    DocumentReferenceType = UBLTR_INVOICE[NS.UBL_CAC].types['DocumentReferenceType']
    ExternalReferenceType = UBLTR_INVOICE[NS.UBL_CAC].types['ExternalReferenceType']
    InvoiceLineType = UBLTR_INVOICE[NS.UBL_CAC].types['InvoiceLineType']
    ItemType = UBLTR_INVOICE[NS.UBL_CAC].types['ItemType']
    MonetaryTotalType = UBLTR_INVOICE[NS.UBL_CAC].types['MonetaryTotalType']
    PartyIdentificationType = UBLTR_INVOICE[NS.UBL_CAC].types['PartyIdentificationType']
    PartyNameType = UBLTR_INVOICE[NS.UBL_CAC].types['PartyNameType']
    PartyTaxSchemeType = UBLTR_INVOICE[NS.UBL_CAC].types['PartyTaxSchemeType']
    PartyType = UBLTR_INVOICE[NS.UBL_CAC].types['PartyType']
    PriceType = UBLTR_INVOICE[NS.UBL_CAC].types['PriceType']
    SignatureType = UBLTR_INVOICE[NS.UBL_CAC].types['SignatureType']
    SupplierPartyType = UBLTR_INVOICE[NS.UBL_CAC].types['SupplierPartyType']
    TaxCategoryType = UBLTR_INVOICE[NS.UBL_CAC].types['TaxCategoryType']
    TaxSchemeType = UBLTR_INVOICE[NS.UBL_CAC].types['TaxSchemeType']
    TaxSubtotalType = UBLTR_INVOICE[NS.UBL_CAC].types['TaxSubtotalType']
    TaxTotalType = UBLTR_INVOICE[NS.UBL_CAC].types['TaxTotalType']


class cbc:
    AllowanceTotalAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['AllowanceTotalAmountType']
    BuildingNameType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'BuildingNameType']
    BuildingNumberType = UBLTR_INVOICE[NS.UBL_CBC].types['BuildingNumberType']

    CalculationSequenceNumericType = UBLTR_INVOICE[NS.UBL_CBC].types['CalculationSequenceNumericType']
    CityNameType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'CityNameType']
    CitySubdivisionNameType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'CitySubdivisionNameType']
    CustomizationIDType = UBLTR_INVOICE[NS.UBL_CBC].types['CustomizationIDType']
    CopyIndicatorType = UBLTR_INVOICE[NS.UBL_CBC].types['CopyIndicatorType']

    DocumentCurrencyCodeType = UBLTR_INVOICE[NS.UBL_CBC].types['DocumentCurrencyCodeType']

    ElectronicMailType = UBLTR_INVOICE[NS.UBL_CBC].types['ElectronicMailType']
    EmbeddedDocumentBinaryObjectType = UBLTR_INVOICE[NS.UBL_CBC].types['EmbeddedDocumentBinaryObjectType']

    IDType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'IDType']
    IDType = UBLTR_INVOICE[NS.UBL_CBC].types['IDType']
    InvoiceTypeCodeType = UBLTR_INVOICE[NS.UBL_CBC].types['InvoiceTypeCodeType']
    InvoicedQuantityType = UBLTR_INVOICE[NS.UBL_CBC].types['InvoicedQuantityType']
    IssueDateType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'IssueDateType']

    LineCountNumericType = UBLTR_INVOICE[NS.UBL_CBC].types['LineCountNumericType']
    LineExtensionAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['LineExtensionAmountType']

    NameType = UBLTR_INVOICE[NS.UBL_CBC].types['NameType']
    NoteType = UBLTR_INVOICE[NS.UBL_CBC].types['NoteType']

    PayableAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['PayableAmountType']
    PercentType = UBLTR_INVOICE[NS.UBL_CBC].types['PercentType']
    PostalZoneType = UBLTR_INVOICE[NS.UBL_CBC].types['PostalZoneType']
    PriceAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['PriceAmountType']
    ProfileIDType = UBLTR_INVOICE[NS.UBL_CBC].types['ProfileIDType']
    ProfileIDType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'ProfileIDType']

    RegionType = UBLTR_INVOICE[NS.UBL_CBC].types['RegionType']
    RegionType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'RegionType']
    RoomType = UBLTR_INVOICE[NS.UBL_CBC].types['RoomType']

    StreetNameType = UBLTR_INVOICE[NS.UBL_CBC].types['StreetNameType']

    TaxAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['TaxAmountType']
    TaxExclusiveAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['TaxExclusiveAmountType']
    TaxInclusiveAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['TaxInclusiveAmountType']
    TaxTypeCodeType = UBLTR_INVOICE[NS.UBL_CBC].types['TaxTypeCodeType']
    TaxableAmountType = UBLTR_INVOICE[NS.UBL_CBC].types['TaxableAmountType']
    TelefaxType = UBLTR_INVOICE[NS.UBL_CBC].types['TelefaxType']
    TelephoneType = UBLTR_INVOICE[NS.UBL_CBC].types['TelephoneType']

    UBLVersionIDType = UBLTR_INVOICE[NS.UBL_CBC].types['UBLVersionIDType']
    UUIDType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'UUIDType']
    URIType = UBLTR_APP_RESPONSE[NS.UBL_CBC].types[u'URIType']


class cec:
    ExtensionContentType = UBLTR_APP_RESPONSE[NS.UBL_CEC].types[u'ExtensionContentType']
    UBLExtensionType = UBLTR_APP_RESPONSE[NS.UBL_CEC].types[u'UBLExtensionType']
    UBLExtensionsType = UBLTR_APP_RESPONSE[NS.UBL_CEC].types[u'UBLExtensionsType']


class udtsm:
    AmountType = UBLTR_INVOICE[NS.UDTSM].types['AmountType']
    BinaryObjectType = UBLTR_INVOICE[NS.UDTSM].types['BinaryObjectType']
    CodeType = UBLTR_INVOICE[NS.UDTSM].types['CodeType']
    IdentifierType = UBLTR_INVOICE[NS.UDTSM].types['IdentifierType']
    NameType = UBLTR_INVOICE[NS.UDTSM].types['NameType']
    QuantityType = UBLTR_INVOICE[NS.UDTSM].types['QuantityType']
    TextType = UBLTR_INVOICE[NS.UDTSM].types['TextType']


class qdt:
    CurrencyCodeType = UBLTR_INVOICE[NS.QDT].types[u'CurrencyCodeType']


class xmldsig:
    DigestMethodType = UBLTR_APP_RESPONSE[NS.XMLDSIG].types[u'DigestMethodType']
    KeyInfoType = UBLTR_APP_RESPONSE[NS.XMLDSIG].types[u'KeyInfoType']
    KeyValueType = UBLTR_INVOICE[NS.XMLDSIG].types['KeyValueType']
    ObjectType = UBLTR_INVOICE[NS.XMLDSIG].types['ObjectType']
    RSAKeyValueType = UBLTR_INVOICE[NS.XMLDSIG].types['RSAKeyValueType']
    ReferenceType = UBLTR_APP_RESPONSE[NS.XMLDSIG].types[u'ReferenceType']
    SignatureMethodType = UBLTR_INVOICE[NS.XMLDSIG].types['SignatureMethodType']
    SignatureType = UBLTR_APP_RESPONSE[NS.XMLDSIG].types[u'SignatureType']
    SignatureValueType = UBLTR_INVOICE[NS.XMLDSIG].types['SignatureValueType']
    SignedInfoType = UBLTR_APP_RESPONSE[NS.XMLDSIG].types[u'SignedInfoType']
    TransformType = UBLTR_INVOICE[NS.XMLDSIG].types['TransformType']
    TransformsType = UBLTR_APP_RESPONSE[NS.XMLDSIG].types[u'TransformsType']
    CanonicalizationMethodType = UBLTR_INVOICE[NS.XMLDSIG].types['CanonicalizationMethodType']
    X509DataType = UBLTR_INVOICE[NS.XMLDSIG].types['X509DataType']
    X509IssuerSerialType = UBLTR_INVOICE[NS.XMLDSIG].types['X509IssuerSerialType']

class xades:
    QualifyingPropertiesType = UBLTR_INVOICE[NS.XADES].types['QualifyingPropertiesType']
    SignedPropertiesType = UBLTR_INVOICE[NS.XADES].types['SignedPropertiesType']
    SignedSignaturePropertiesType = UBLTR_INVOICE[NS.XADES].types['SignedSignaturePropertiesType']
    CertIDType = UBLTR_INVOICE[NS.XADES].types['CertIDType']
    CertIDListType = UBLTR_INVOICE[NS.XADES].types['CertIDListType']
    DigestAlgAndValueType = UBLTR_INVOICE[NS.XADES].types['DigestAlgAndValueType']
    SignerRoleType = UBLTR_INVOICE[NS.XADES].types['SignerRoleType']
    ClaimedRolesListType = UBLTR_INVOICE[NS.XADES].types['ClaimedRolesListType']
    AnyType = UBLTR_INVOICE[NS.XADES].types['AnyType']


xmldsig.ObjectType._type_info['QualifyingProperties'] = \
                       xades.QualifyingPropertiesType.customize(sub_ns=NS.XADES)

