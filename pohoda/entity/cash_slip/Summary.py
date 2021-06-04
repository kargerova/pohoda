# coding: utf-8

from pohoda.entity.Agenda import Agenda
from pohoda.entity.type.CurrencyHome import CurrencyHome


class Summary(Agenda):
    _elements = ['roundingDocument', 'roundingVAT', 'calculateVAT', 'homeCurrency']

    def __init__(self, data: dict, ico: str):
        # process home currency
        home_currency = data.get('homeCurrency')
        if home_currency:
            data['homeCurrency'] = CurrencyHome(home_currency, ico)

        super().__init__(data, ico)

    def get_xml(self):
        xml = self._create_xml_tag('prodejkaSummary', namespace='pro')
        self._add_elements(xml, self._elements, 'pro')
        return xml
