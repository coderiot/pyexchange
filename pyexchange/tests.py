#!/usr/bin/env python
# encoding: utf-8

import datetime

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
                   'rocktrading',
                   'coinse']

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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)
            self.assertIsInstance(t.tid, int)


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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)
            self.assertIsNone(t.tid)


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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)
            self.assertIsInstance(t.tid, int)


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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)
            self.assertIsInstance(t.tid, int)


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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)
            self.assertIsInstance(t.tid, int)


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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        self.assertItemsEqual(trades, [])


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
                       'dvc_btc', 'wdc_btc', 'dgc_btc',
                       'wdc_usd']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.cryptotrade.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


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

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestIntersango(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.intersango.Intersango()

    def test_markets(self):
        exp_markets = ['btc_usd', 'btc_eur', 'btc_gbp', 'btc_pln']

        obj_markets = self.ex.markets()
        module_markets = pyexchange.intersango.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestJustcoin(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.justcoin.Justcoin()

    def test_markets(self):
        exp_markets = ['btc_eur', 'btc_nok', 'btc_ltc', 'btc_xrp']

        obj_markets = self.ex.markets()
        module_markets = pyexchange.justcoin.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestLocalbitcoins(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.localbitcoins.LocalBitcoins()

    def test_markets(self):
        exp_markets = ['btc_ars', 'btc_aud', 'btc_brl',
                       'btc_cad', 'btc_eur', 'btc_gbp',
                       'btc_ghs', 'btc_huf', 'btc_mxn',
                       'btc_nzd', 'btc_php', 'btc_pln',
                       'btc_rub', 'btc_sgd', 'btc_thb',
                       'btc_usd', 'btc_zar']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.localbitcoins.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestMtGox(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.mtgox.MtGox()

    def test_markets(self):
        exp_markets = ['btc_usd', 'btc_gpb', 'btc_eur',
                       'btc_jpy', 'btc_aud', 'btc_cad',
                       'btc_chf', 'btc_cny', 'btc_dkk',
                       'btc_hkd', 'btc_pln', 'btc_rub',
                       'btc_sek', 'btc_sgd', 'btc_thb',
                       'btc_nok', 'btc_czk']
        obj_markets = self.ex.markets()
        module_markets = pyexchange.mtgox.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestRocktrading(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.rocktrading.RockTrading()

    def test_markets(self):
        exp_markets = ['btc_eur', 'btc_usd', 'btc_xrp',
                       'eur_xrp', 'ltc_btc', 'ltc_eur']

        obj_markets = self.ex.markets()
        module_markets = pyexchange.rocktrading.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestBter(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.bter.Bter()

    def test_markets(self):
        exp_markets = ["btc_cny", "ltc_cny", "ftc_cny", "frc_cny",
                       "ppc_cny", "trc_cny", "wdc_cny", "yac_cny",
                       "cnc_cny", "bqc_cny", "ifc_cny", "zcc_cny",
                       "cmc_cny", "jry_cny", "xpm_cny",
                       "pts_cny", "tag_cny", "tix_cny", "src_cny",
                       "mec_cny", "nmc_cny", "qrk_cny", "btb_cny",
                       "exc_cny", "dtc_cny", "cent_cny", "red_cny",
                       "zet_cny", "ftc_ltc", "frc_ltc", "ppc_ltc",
                       "trc_ltc", "nmc_ltc", "wdc_ltc", "yac_ltc",
                       "cnc_ltc", "bqc_ltc", "ifc_ltc", "red_ltc",
                       "tix_ltc", "cent_ltc", "ltc_btc", "nmc_btc",
                       "ppc_btc", "trc_btc", "frc_btc", "ftc_btc",
                       "bqc_btc", "cnc_btc", "btb_btc", "yac_btc",
                       "wdc_btc", "zcc_btc", "xpm_btc", "zet_btc",
                       "src_btc", "sav_btc", "cdc_btc", "cmc_btc",
                       "jry_btc", "tag_btc", "pts_btc", "dtc_btc",
                       "exc_btc", "nec_btc", "mec_btc", "qrk_btc",
                       "anc_btc", "nvc_btc", "buk_btc", "myminer_btc"]

        obj_markets = self.ex.markets()
        module_markets = pyexchange.bter.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)


class TestCoinse(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.coinse.Coinse()

    def test_markets(self):
        exp_markets = ["alp_btc", "alp_ltc", "amc_btc", "amc_ltc",
                       "anc_btc", "anc_ltc", "arg_btc", "arg_ltc",
                       "bet_btc", "bet_ltc", "bqc_btc", "btg_btc",
                       "cgb_btc", "cin_btc", "cmc_btc", "col_ltc",
                       "crc_btc", "csc_btc", "dem_btc", "dem_ltc",
                       "dgc_btc", "dmd_btc", "dtc_btc", "elc_btc",
                       "elp_btc", "emd_btc", "ezc_btc", "flo_btc",
                       "frk_btc", "frk_ltc", "ftc_btc", "gdc_btc",
                       "glc_btc", "glc_ltc", "glx_btc", "hyc_btc",
                       "ifc_btc", "ifc_ltc", "ifc_xpm", "kgc_btc",
                       "kgc_ltc", "lbw_btc", "ltc_btc", "mec_btc",
                       "nan_btc", "net_btc", "nib_btc", "nrb_btc",
                       "nuc_btc", "nvc_btc", "orb_btc", "orb_ltc",
                       "ppc_btc", "ppc_xpm", "pts_btc", "pwc_btc",
                       "pxc_btc", "pxc_ltc", "qrk_btc", "qrk_ltc",
                       "qrk_xpm", "rch_btc", "rch_ltc", "rec_btc",
                       "rec_ltc", "red_btc", "red_ltc", "sbc_btc",
                       "sbc_ltc", "spt_btc", "tag_btc", "trc_btc",
                       "uno_btc", "vlc_btc", "vlc_ltc", "wdc_btc",
                       "xnc_btc", "xnc_ltc", "xpm_btc", "xpm_ltc",
                       "zet_btc"]

        obj_markets = self.ex.markets()
        module_markets = pyexchange.coinse.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)

class TestVircurex(unittest.TestCase):
    """Test case docstring"""

    def setUp(self):
        self.ex = pyexchange.vircurex.Vircurex()

    def test_markets(self):
        exp_markets = ["frc_ppc", "frc_dgc", "frc_usd", "frc_ltc", "frc_xpm",
                       "frc_anc", "frc_ixc", "frc_trc", "frc_dvc", "frc_i0c",
                       "frc_ftc", "frc_wdc", "frc_nvc", "frc_nmc", "frc_btc",
                       "frc_eur", "dgc_frc", "dgc_i0c", "dgc_usd", "dgc_xpm",
                       "dgc_anc", "dgc_ixc", "dgc_trc", "dgc_dvc", "dgc_ltc",
                       "dgc_ftc", "dgc_ppc", "dgc_nvc", "dgc_nmc", "dgc_btc",
                       "dgc_wdc", "dgc_eur", "usd_frc", "usd_dgc", "usd_wdc",
                       "usd_ltc", "usd_xpm", "usd_anc", "usd_ixc", "usd_trc",
                       "usd_dvc", "usd_i0c", "usd_ftc", "usd_ppc", "usd_nvc",
                       "usd_nmc", "usd_btc", "usd_eur", "ltc_frc", "ltc_dgc",
                       "ltc_usd", "ltc_xpm", "ltc_anc", "ltc_ixc", "ltc_trc",
                       "ltc_dvc", "ltc_i0c", "ltc_ftc", "ltc_ppc", "ltc_nvc",
                       "ltc_nmc", "ltc_btc", "ltc_wdc", "ltc_eur", "xpm_frc",
                       "xpm_dgc", "xpm_usd", "xpm_ltc", "xpm_anc", "xpm_ixc",
                       "xpm_trc", "xpm_dvc", "xpm_i0c", "xpm_ftc", "xpm_ppc",
                       "xpm_nvc", "xpm_nmc", "xpm_btc", "xpm_wdc", "xpm_eur",
                       "anc_frc", "anc_dgc", "anc_usd", "anc_xpm", "anc_i0c",
                       "anc_ixc", "anc_trc", "anc_dvc", "anc_ltc", "anc_ftc",
                       "anc_ppc", "anc_nvc", "anc_nmc", "anc_btc", "anc_wdc",
                       "anc_eur", "ixc_frc", "ixc_dgc", "ixc_usd", "ixc_ltc",
                       "ixc_xpm", "ixc_anc", "ixc_trc", "ixc_dvc", "ixc_i0c",
                       "ixc_ftc", "ixc_ppc", "ixc_nvc", "ixc_nmc", "ixc_btc",
                       "ixc_wdc", "ixc_eur", "trc_frc", "trc_dgc", "trc_usd",
                       "trc_ltc", "trc_xpm", "trc_anc", "trc_ixc", "trc_dvc",
                       "trc_i0c", "trc_ftc", "trc_ppc", "trc_nvc", "trc_nmc",
                       "trc_btc", "trc_wdc", "trc_eur", "dvc_frc", "dvc_dgc",
                       "dvc_usd", "dvc_ltc", "dvc_xpm", "dvc_anc", "dvc_ixc",
                       "dvc_trc", "dvc_i0c", "dvc_ftc", "dvc_ppc", "dvc_nvc",
                       "dvc_nmc", "dvc_btc", "dvc_wdc", "dvc_eur", "i0c_frc",
                       "i0c_dgc", "i0c_usd", "i0c_xpm", "i0c_anc", "i0c_ixc",
                       "i0c_trc", "i0c_dvc", "i0c_ltc", "i0c_ftc", "i0c_ppc",
                       "i0c_nvc", "i0c_nmc", "i0c_btc", "i0c_wdc", "i0c_eur",
                       "ftc_frc", "ftc_dgc", "ftc_usd", "ftc_ltc", "ftc_xpm",
                       "ftc_anc", "ftc_ixc", "ftc_trc", "ftc_dvc", "ftc_i0c",
                       "ftc_ppc", "ftc_nvc", "ftc_nmc", "ftc_btc", "ftc_wdc",
                       "ftc_eur", "ppc_frc", "ppc_dgc", "ppc_usd", "ppc_ltc",
                       "ppc_xpm", "ppc_anc", "ppc_ixc", "ppc_trc", "ppc_dvc",
                       "ppc_i0c", "ppc_ftc", "ppc_wdc", "ppc_nvc", "ppc_nmc",
                       "ppc_btc", "ppc_eur", "nvc_frc", "nvc_dgc", "nvc_usd",
                       "nvc_ltc", "nvc_xpm", "nvc_anc", "nvc_ixc", "nvc_trc",
                       "nvc_dvc", "nvc_i0c", "nvc_ftc", "nvc_ppc", "nvc_nmc",
                       "nvc_btc", "nvc_wdc", "nvc_eur", "nmc_frc", "nmc_dgc",
                       "nmc_usd", "nmc_ltc", "nmc_xpm", "nmc_anc", "nmc_ixc",
                       "nmc_trc", "nmc_dvc", "nmc_i0c", "nmc_ftc", "nmc_ppc",
                       "nmc_nvc", "nmc_btc", "nmc_wdc", "nmc_eur", "btc_frc",
                       "btc_dgc", "btc_usd", "btc_ltc", "btc_xpm", "btc_anc",
                       "btc_ixc", "btc_trc", "btc_dvc", "btc_i0c", "btc_ftc",
                       "btc_ppc", "btc_nvc", "btc_nmc", "btc_wdc", "btc_eur",
                       "wdc_frc", "wdc_dgc", "wdc_usd", "wdc_ltc", "wdc_xpm",
                       "wdc_anc", "wdc_ixc", "wdc_trc", "wdc_dvc", "wdc_i0c",
                       "wdc_ftc", "wdc_ppc", "wdc_nvc", "wdc_nmc", "wdc_btc",
                       "wdc_eur", "eur_frc", "eur_dgc", "eur_usd", "eur_ltc",
                       "eur_xpm", "eur_anc", "eur_ixc", "eur_trc", "eur_dvc",
                       "eur_i0c", "eur_ftc", "eur_ppc", "eur_nvc", "eur_nmc",
                       "eur_btc", "eur_wdc"]

        obj_markets = self.ex.markets()
        module_markets = pyexchange.vircurex.markets()
        self.assertItemsEqual(exp_markets, obj_markets)
        self.assertItemsEqual(exp_markets, module_markets)

    def test_ticker(self):
        ticker = self.ex.ticker()
        self.assertIsInstance(ticker, models.Ticker)
        for k, v in ticker._asdict().items():
            self.assertIsInstance(v, decimal.Decimal)

    def test_depth(self):
        asks, bids = self.ex.depth()
        self.assertIsInstance(asks, list)
        self.assertIsInstance(bids, list)
        for a in asks:
            self.assertIsInstance(a, models.Order)
            self.assertIsInstance(a.price, decimal.Decimal)
            self.assertIsInstance(a.amount, decimal.Decimal)

        for b in bids:
            self.assertIsInstance(b, models.Order)
            self.assertIsInstance(b.price, decimal.Decimal)
            self.assertIsInstance(b.amount, decimal.Decimal)

    def test_trades(self):
        trades = self.ex.trades()
        self.assertIsInstance(trades, list)
        for t in trades:
            self.assertIsInstance(t, models.Trade)
            self.assertIsInstance(t.date, datetime.datetime)
            self.assertIsInstance(t.price, decimal.Decimal)
            self.assertIsInstance(t.amount, decimal.Decimal)
            self.assertIsInstance(t.tid, int)

if __name__ == '__main__':
    unittest.main(verbosity=2)
