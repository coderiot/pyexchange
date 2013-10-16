#!/usr/bin/env python
# encoding: utf-8

import models

import requests


class RockTrading(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_eur': 'BTCEUR',
                    'btc_usd': 'BTCUSD',
                    'btc_xrp': 'BTCXRP',
                    'eur_xrp': 'EURXRP',
                    'ltc_btc': 'LTCBTC',
                    'ltc_eur': 'LTCEUR'}

    _endpoint = "http://www.therocktrading.com/api/%(method)s/%(market)s"

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        m = self._markets_map[self.market]
        url = RockTrading._endpoint % {'market': m, 'method': 'orderbook'}
        resp = requests.get(url, verify=False).json()

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
        m = self._markets_map[self.market]
        url = RockTrading._endpoint % {'market': m, 'method': 'ticker'}
        resp = requests.get(url, verify=False).json()['result'][0]

        return models.Ticker(avg=None,
                             buy=float(resp['bid']),
                             high=None,
                             last=None,
                             low=None,
                             sell=float(resp['ask']),
                             vol=None)

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        m = self._markets_map[self.market]
        url = RockTrading._endpoint % {'market': m, 'method': 'trades'}
        return requests.get(url, verify=False).json()
