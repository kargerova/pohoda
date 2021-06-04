# coding: utf-8

from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['number', 'priceLevel', 'paymentType', 'centre', 'activity', 'contract', 'carrier', 'regVATinEU']
    _elements = ['number', 'date', 'numberOrder', 'dateOrder', 'text', 'partnerIdentity', 'acc', 'symPar', 'priceLevel',
                 'paymentType', 'isExecuted', 'isDelivered', 'centre', 'activity', 'contract', 'carrier', 'regVATinEU',
                 'note', 'intNote']

    def __init__(self, data: dict, ico: str):
        # process partner identity
        partner_identity = data.get('partnerIdentity')
        if partner_identity:
            data['partnerIdentity'] = Address(partner_identity, ico)

        super().__init__(data, ico)

    def get_xml(self):
        xml = self._create_xml_tag('vydejkaHeader', 'vyd')
        self._add_elements(xml, self._elements + ['parameters'], 'vyd')
        return xml
