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


class TestBitstamp(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.bitstamp.Bitstamp()

    def test_markets(self):
        exp_markets = ['btc_usd']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.bitstamp.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)


class TestBtcchina(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.btcchina.BtcChina()

    def test_markets(self):
        exp_markets = ['btc_cny']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.btcchina.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)


class TestBtce(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.btce.Btce()

    def test_markets(self):
        exp_markets = ['btc_usd', 'btc_eur', 'btc_rur',
                       'ltc_btc', 'ltc_usd', 'ltc_rur',
                       'ltc_eur', 'nmc_btc', 'nmc_usd',
                       'nvc_btc', 'nvc_usd', 'usd_rur',
                       'eur_usd', 'trc_btc', 'ppc_btc',
                       'ftc_btc']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.btce.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)


class TestCampbx(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.campbx.Campbx()

    def test_markets(self):
        exp_markets = ['btc_usd']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.campbx.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)


class TestCryptotrade(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.cryptotrade.Cryptotrade()

    def test_markets(self):
        exp_markets = ['btc_usd', 'btc_eur', 'ltc_usd',
                       'ltc_eur', 'ltc_btc', 'nmc_usd',
                       'nmc_btc', 'xpm_usd', 'xpm_btc',
                       'xpm_ppc', 'ppc_usd', 'ppc_btc',
                       'trc_btc', 'ftc_usd', 'ftc_btc',
                       'dvc_btc', 'wdc_btc', 'dgc_btc']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.cryptotrade.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)


class TestCryptsy(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.cryptsy.Cryptsy()

    def test_markets(self):
        exp_markets = ['frk_btc', 'lky_btc', 'nvc_btc',
                       'ftc_btc', 'cgb_btc', 'frc_btc',
                       'sbc_btc', 'dbl_ltc', 'jkc_ltc',
                       'phs_btc', 'net_ltc', 'spt_btc',
                       'mec_ltc', 'alf_btc', 'ybc_btc',
                       'elp_ltc', 'fst_btc', 'gld_ltc',
                       'anc_btc', 'tix_xpm', 'nec_btc',
                       'sxc_ltc', 'zet_btc', 'ifc_ltc',
                       'cap_btc', 'ppc_btc', 'kgc_btc',
                       'qrk_btc', 'red_ltc', 'net_xpm',
                       'wdc_btc', 'cent_ltc',
                       'elc_btc', 'mec_btc', 'xpm_ltc',
                       'nmc_btc', 'dgc_ltc', 'ltc_btc',
                       'dmd_btc', 'clr_btc', 'gme_ltc',
                       'gdc_btc', 'wdc_ltc', 'arg_btc',
                       'pxc_ltc', 'mst_ltc', 'csc_btc',
                       'nbl_btc', 'cmc_btc', 'ezc_ltc',
                       'amc_btc', 'trc_btc', 'xnc_ltc',
                       'tix_ltc', 'ifc_xpm', 'mem_ltc',
                       'src_btc', 'cpr_ltc', 'dgc_btc',
                       'yac_btc', 'adt_ltc', 'pxc_btc',
                       'bte_btc', 'flo_ltc', 'bqc_btc',
                       'btg_btc', 'nrb_btc', 'crc_btc',
                       'glc_btc', 'xpm_btc', 'btb_btc',
                       'pyc_btc', 'ryc_ltc', 'gld_btc',
                       'ixc_btc', 'mnc_btc', 'glx_btc',
                       'emd_btc', 'buk_btc', 'dvc_ltc']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.cryptsy.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

if __name__ == '__main__':
    unittest.main(verbosity=2)
