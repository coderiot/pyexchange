#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://coinex.pw/api/v2/"


class Coinex(models.Exchange):
    """Coinex API Documentation:
       https://gist.github.com/erundook/8377222"""
    _markets_map = {"ifc_ltc": 13,
                    "boc_btc": 16,
                    "pyc_btc": 31,
                    "grw_btc": 2,
                    "cat_doge": 67,
                    "xpm_btc": 7,
                    "phs_btc": 9,
                    "mnc_btc": 29,
                    "ifc_btc": 10,
                    "wdc_doge": 65,
                    "src_btc": 24,
                    "ifc_doge": 66,
                    "boc_ltc": 12,
                    "gld_ltc": 18,
                    "fre_btc": 26,
                    "lot_btc": 59,
                    "uno_doge": 70,
                    "nvc_btc": 33,
                    "cmc_btc": 25,
                    "zet_doge": 71,
                    "cgb_btc": 14,
                    "exc_btc": 8,
                    "wdc_btc": 15,
                    "bet_btc": 56,
                    "zet_btc": 6,
                    "ftc_btc": 1,
                    "asc_btc": 21,
                    "eac_btc": 52,
                    "asc_doge": 68,
                    "mec_btc": 32,
                    "ffc_doge": 63,
                    "moon_doge": 61,
                    "eac_doge": 62,
                    "sxc_ltc": 58,
                    "osc_btc": 38,
                    "sxc_doge": 64,
                    "ppc_btc": 35,
                    "bfc_btc": 17,
                    "tek_btc": 43,
                    "dem_btc": 44,
                    "moon_btc": 54,
                    "anc_btc": 36,
                    "fst_btc": 20,
                    "doge_btc": 46,
                    "sxc_btc": 5,
                    "tgc_ltc": 45,
                    "cat_ltc": 51,
                    "tgc_btc": 19,
                    "moon_ltc": 55,
                    "gld_btc": 4,
                    "cap_btc": 3,
                    "lot_doge": 69,
                    "lky_btc": 27,
                    "nec_btc": 22,
                    "pxc_btc": 30,
                    "trc_btc": 11,
                    "bte_btc": 34,
                    "hbn_btc": 37,
                    "bet_ltc": 57,
                    "ltc_btc": 28,
                    "lot_ltc": 60,
                    "dgc_btc": 23,
                    "uno_btc": 40,
                    "ffc_btc": 47,
                    "doge_ltc": 49,
                    "eac_ltc": 53,
                    "ffc_ltc": 48,
                    "xjo_btc": 41,
                    "asc_ltc": 39,
                    "cat_btc": 50}


    def __init__(self, market="ltc_btc"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = base_url + "orders?tradePair=" + str(self._symbol)
        resp = self._request('GET', url).json()

        asks = []
        bids = []

        for o in resp['orders']:
            if o['bid']:
                bids.append(models.Order(
                    price=self._create_decimal(o['rate'] * 10E-8),
                    amount=self._create_decimal(o['amount'] * 10E-8)))
            else:
                asks.append(models.Order(
                    price=self._create_decimal(o['rate'] * 10E-8),
                    amount=self._create_decimal(o['amount'] * 10E-8)))

        return asks, bids

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = base_url + "trades?tradePair=" + str(self._symbol)
        resp = self._request('GET', url).json()

        fmt = "%Y-%m-%dT%H:%M:%S.%fZ"

        trades = []
        for t in resp['trades']:
            date = datetime.strptime(t['created_at'], fmt)
            amount = self._create_decimal(t['amount'] * 10E-8)
            price = self._create_decimal(t['rate'] * 10E-8)
            tid = t['id']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
