#!/usr/bin/env python
# encoding: utf-8

import models

import requests


# einheitliche markets for all exchanges
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
                    'dgc_btc': 'dgc_btc'}

    _endpoint = "https://crypto-trade.com/api/1/%(method)s/%(market)s"

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = Cryptotrade._endpoint % {'market': self.market,
                                       'method': 'depth'}
        resp = requests.get(url).json()

        asks = []
        for p, a in resp['asks']:
            asks.append(models.Order(price=p,
                                     amount=a))
        bids = []
        for p, a in resp['bids']:
            bids.append(models.Order(price=p,
                                     amount=a))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = Cryptotrade._endpoint % {'market': self.market,
                                       'method': 'ticker'}
        j = requests.get(url).json()
        resp = j['data']
        return models.Ticker(avg=None,# high + low / 2.
                             high=float(resp['high']),
                             low=float(resp['low']),
                             last=float(resp['last']),
                             buy=float(resp['max_bid']),
                             sell=float(resp['min_ask']),
                             vol=float(resp['vol_btc']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []
