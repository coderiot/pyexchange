#!/usr/bin/env python
# encoding: utf-8

import decimal

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

    def test_exchanges_check_elements(self):
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

    def test_unknow_exchange(self):
        #ex = pyexchange.new_exchange('unknown')
        self.assertRaises(Exception, pyexchange.new_exchange, 'unknown')


class TestBitcurex(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.new_exchange('bitcurex')

    def test_markets(self):
        exp_markets = ['btc_eur', 'btc_pln']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.bitcurex.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)


class TestBitfinex(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.bitfinex.Bitfinex()

    def test_markets(self):
        exp_markets = ['ltc_btc', 'ltc_usd', 'btc_usd']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.bitfinex.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

if __name__ == '__main__':
    unittest.main(verbosity=2)
