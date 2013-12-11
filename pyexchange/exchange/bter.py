#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://bter.com/api/1"


class Bter(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {"btc_cny": "btc_cny",
                    "ltc_cny": "ltc_cny",
                    "ftc_cny": "ftc_cny",
                    "frc_cny": "frc_cny",
                    "ppc_cny": "ppc_cny",
                    "trc_cny": "trc_cny",
                    "wdc_cny": "wdc_cny",
                    "yac_cny": "yac_cny",
                    "cnc_cny": "cnc_cny",
                    "bqc_cny": "bqc_cny",
                    "ifc_cny": "ifc_cny",
                    "zcc_cny": "zcc_cny",
                    "cmc_cny": "cmc_cny",
                    "jry_cny": "jry_cny",
                    "xpm_cny": "xpm_cny",
                    "ppc_cny": "ppc_cny",
                    "pts_cny": "pts_cny",
                    "tag_cny": "tag_cny",
                    "tix_cny": "tix_cny",
                    "src_cny": "src_cny",
                    "mec_cny": "mec_cny",
                    "nmc_cny": "nmc_cny",
                    "qrk_cny": "qrk_cny",
                    "btb_cny": "btb_cny",
                    "exc_cny": "exc_cny",
                    "dtc_cny": "dtc_cny",
                    "cent_cny": "cent_cny",
                    "red_cny": "red_cny",
                    "zet_cny": "zet_cny",
                    "ftc_ltc": "ftc_ltc",
                    "frc_ltc": "frc_ltc",
                    "ppc_ltc": "ppc_ltc",
                    "trc_ltc": "trc_ltc",
                    "nmc_ltc": "nmc_ltc",
                    "wdc_ltc": "wdc_ltc",
                    "yac_ltc": "yac_ltc",
                    "cnc_ltc": "cnc_ltc",
                    "bqc_ltc": "bqc_ltc",
                    "ifc_ltc": "ifc_ltc",
                    "red_ltc": "red_ltc",
                    "tix_ltc": "tix_ltc",
                    "cent_ltc": "cent_ltc",
                    "ltc_btc": "ltc_btc",
                    "nmc_btc": "nmc_btc",
                    "ppc_btc": "ppc_btc",
                    "trc_btc": "trc_btc",
                    "frc_btc": "frc_btc",
                    "ftc_btc": "ftc_btc",
                    "bqc_btc": "bqc_btc",
                    "cnc_btc": "cnc_btc",
                    "btb_btc": "btb_btc",
                    "yac_btc": "yac_btc",
                    "wdc_btc": "wdc_btc",
                    "zcc_btc": "zcc_btc",
                    "xpm_btc": "xpm_btc",
                    "zet_btc": "zet_btc",
                    "src_btc": "src_btc",
                    "sav_btc": "sav_btc",
                    "cdc_btc": "cdc_btc",
                    "cmc_btc": "cmc_btc",
                    "jry_btc": "jry_btc",
                    "tag_btc": "tag_btc",
                    "pts_btc": "pts_btc",
                    "dtc_btc": "dtc_btc",
                    "exc_btc": "exc_btc",
                    "nec_btc": "nec_btc",
                    "mec_btc": "mec_btc",
                    "qrk_btc": "qrk_btc",
                    "anc_btc": "anc_btc",
                    "nvc_btc": "nvc_btc",
                    "buk_btc": "buk_btc",
                    "myminer_btc": "myminer_btc"}

    def __init__(self, market="ltc_btc"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "/".join([base_url, 'depth', self._symbol])
        resp = self._request('GET', url).json()

        asks = []
        for p, a in resp['asks']:
            asks.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))
        bids = []
        for p, a in resp['bids']:
            bids.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "/".join([base_url, 'ticker', self._symbol])
        resp = self._request('GET', url).json()

        return models.Ticker(avg=self._create_decimal(resp['avg']),
                      high=self._create_decimal(resp['high']),
                      low=self._create_decimal(resp['low']),
                      last=self._create_decimal(resp['last']),
                      buy=self._create_decimal(resp['buy']),
                      sell=self._create_decimal(resp['sell']),
                      )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'trade', self._symbol])
        resp = self._request('GET', url).json()

        trades = []
        for t in resp['data']:
            date = datetime.fromtimestamp(int(t['date']))
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = int(t['tid'])
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades

