#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

public_url = "http://pubapi.cryptsy.com/api.php"


class Cryptsy(models.Exchange):
    """Docstring for Cryptsy"""

    _markets_map = {
                    "frk_btc": 33,
                    "lky_btc": 34,
                    "nvc_btc": 13,
                    "ftc_btc": 5,
                    "cgb_btc": 70,
                    "frc_btc": 39,
                    "sbc_btc": 51,
                    "dbl_ltc": 46,
                    "jkc_ltc": 35,
                    "phs_btc": 86,
                    "net_ltc": 108,
                    "spt_btc": 81,
                    "mec_ltc": 100,
                    "alf_btc": 57,
                    "ybc_btc": 73,
                    "elp_ltc": 93,
                    "fst_btc": 44,
                    "gld_ltc": 36,
                    "anc_btc": 66,
                    "tix_xpm": 103,
                    "nec_btc": 90,
                    "sxc_ltc": 98,
                    "zet_btc": 85,
                    "ifc_ltc": 60,
                    "cap_btc": 53,
                    "ppc_btc": 28,
                    "kgc_btc": 65,
                    "qrk_btc": 71,
                    "red_ltc": 87,
                    "net_xpm": 104,
                    "wdc_btc": 14,
                    "cent_ltc": 97,
                    "elc_btc": 12,
                    "mec_btc": 45,
                    "xpm_ltc": 106,
                    "nmc_btc": 29,
                    "dgc_ltc": 96,
                    "ltc_btc": 3,
                    "dmd_btc": 72,
                    "clr_btc": 95,
                    "gme_ltc": 84,
                    "gdc_btc": 82,
                    "wdc_ltc": 21,
                    "arg_btc": 48,
                    "pxc_ltc": 101,
                    "mst_ltc": 62,
                    "csc_btc": 68,
                    "nbl_btc": 32,
                    "cmc_btc": 74,
                    "ezc_ltc": 55,
                    "amc_btc": 43,
                    "trc_btc": 27,
                    "xnc_ltc": 67,
                    "tix_ltc": 107,
                    "ifc_xpm": 105,
                    "mem_ltc": 56,
                    "src_btc": 88,
                    "cpr_ltc": 91,
                    "dgc_btc": 26,
                    "yac_btc": 11,
                    "adt_ltc": 94,
                    "pxc_btc": 31,
                    "bte_btc": 49,
                    "flo_ltc": 61,
                    "bqc_btc": 10,
                    "btg_btc": 50,
                    "nrb_btc": 54,
                    "crc_btc": 58,
                    "glc_btc": 76,
                    "xpm_btc": 63,
                    "btb_btc": 23,
                    "pyc_btc": 92,
                    "ryc_ltc": 37,
                    "gld_btc": 30,
                    "ixc_btc": 38,
                    "mnc_btc": 7,
                    "glx_btc": 78,
                    "emd_btc": 69,
                    "buk_btc": 102,
                    "dvc_ltc": 52,
                   }

    def __init__(self, market="ltc_btc"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todoo

        """
        url = "%s?method=%s&marketid=%s" % (public_url,
                                            'singlemarketdata',
                                            self._symbol)
        resp = self._request('GET', url).json()
        key = resp['return']['markets'].keys()[0]
        resp = resp['return']['markets'][key]

        asks = []
        for order in resp['sellorders']:
            asks.append(models.Order(price=order['price'],
                                     amount=order['quantity']))
        bids = []
        for order in resp['buyorders']:
            bids.append(models.Order(price=order['price'],
                                     amount=order['quantity']))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "%s?method=%s&marketid=%s" % (public_url,
                                            'singlemarketdata',
                                            self._symbol)
        resp = self._request('GET', url).json()
        key = resp['return']['markets'].keys()[0]
        resp = resp['return']['markets'][key]

        return models.Ticker(avg=None,
                             buy=None,
                             high=None,
                             last=resp['lasttradeprice'],
                             low=None,
                             sell=None,
                             vol=resp['volume'])

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "%s?method=%s&marketid=%s" % (public_url,
                                            'singlemarketdata',
                                            self._symbol)
        resp = self._request('GET', url).json()
        key = resp['return']['markets'].keys()[0]
        resp = resp['return']['markets'][key]

        trades = []
        for t in resp['recenttrades']:
            date = datetime.strptime(t['time'], "%Y-%m-%d %H:%M:%S")
            amount = t['quantity']
            price = t['price']
            tid = t['id']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
