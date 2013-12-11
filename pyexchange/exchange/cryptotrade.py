#!/usr/bin/env python
# encoding: utf-8

import models

base_url = "https://crypto-trade.com/api/1"


class Cryptotrade(models.Exchange):
    """Docstring for Cryptotrade"""

    _markets_map = {'btc_usd': 'btc_usd',
                    'btc_eur': 'btc_eur',
                    'ltc_usd': 'ltc_usd',
                    'ltc_eur': 'ltc_eur',
                    'ltc_btc': 'ltc_btc',
                    'nmc_usd': 'nmc_usd',
                    'nmc_btc': 'nmc_btc',
                    'xpm_usd': 'xpm_usd',
                    'xpm_btc': 'xpm_btc',
                    'xpm_ppc': 'xpm_ppc',
                    'ppc_usd': 'ppc_usd',
                    'ppc_btc': 'ppc_btc',
                    'trc_btc': 'trc_btc',
                    'ftc_usd': 'ftc_usd',
                    'ftc_btc': 'ftc_btc',
                    'dvc_btc': 'dvc_btc',
                    'wdc_btc': 'wdc_btc',
                    'wdc_usd': 'wdc_usd',
                    'dgc_btc': 'dgc_btc'}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url, 'depth', self._symbol)
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
        url = "%s/%s/%s" % (base_url, 'ticker', self._symbol)
        resp = self._request('GET', url).json()

        return models.Ticker(
                             high=self._create_decimal(resp['data']['high']),
                             low=self._create_decimal(resp['data']['low']),
                             last=self._create_decimal(resp['data']['last']),
                             buy=self._create_decimal(resp['data']['max_bid']),
                             sell=self._create_decimal(resp['data']['min_ask']),
                             vol=self._create_decimal(resp['data']['vol_btc']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []
