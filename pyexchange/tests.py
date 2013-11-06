#!/usr/bin/env python
# encoding: utf-8

import unittest

import pyexchange

from pyexchange.exchange import models


class TestExchangesList(unittest.TestCase):
    """Test case docstring"""

    def test_exchanges_not_none(self):
        exs = pyexchange.exchanges()
        self.assertIsNotNone(exs)

    def test_exchanges_is_list(self):
        exs = pyexchange.exchanges()
        self.assertIsInstance(exs, list)

    def test_exchanges_not_empty(self):
        exs = pyexchange.exchanges()
        self.assertNotEqual(exs, [])

    def test_exchanges_check_elemets(self):
        exp_exs = ['bitcurex',
                   'bitfinex',
                   'bitstamp',
                   'btcchina',
                   'btce',
                   'campbx',
                   'cryptotrade',
                   'cryptsy',
                   'intersango',
                   'justcoin',
                   'localbitcoins',
                   'mtgox',
                   'rocktrading']

        exs = pyexchange.exchanges()
        self.assertIsInstance(exs, list)
        self.assertListEqual(exp_exs, exs)

    def test_exchange_creation(self):
        for ex in pyexchange.exchanges():
            ex_obj = pyexchange.new_exchange(ex)
            self.assertIsInstance(ex_obj, models.Exchange)

if __name__ == '__main__':
    unittest.main(verbosity=2)
