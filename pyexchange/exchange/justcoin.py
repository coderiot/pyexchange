#!/usr/bin/env python
# encoding: utf-8

import models

import requests


class Justcoin(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {'btc_eur': 'BTCEUR',
                    'btc_nok': 'BTCNOK',
                    'btc_ltc': 'BTCLTC',
                    'btc_xrp': 'BTCXRP'}

    _endpoint = "https://justcoin.com/api/v1/markets/%(market)s%(method)s"

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        m = self._markets_map[self.market]
        url = Justcoin._endpoint % {'market': m, 'method': '/depth'}
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
        m = self._markets_map[self.market]
        url = Justcoin._endpoint % {'market': '', 'method': ''}
        for market in requests.get(url).json():
            if market['id'] == m:
                resp = market

        return models.Ticker(avg=None,
                             buy=float(resp['ask']),
                             high=float(resp['high']),
                             last=float(resp['last']),
                             low=float(resp['low']),
                             sell=float(resp['bid']),
                             vol=float(resp['volume']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []
