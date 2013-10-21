#!/usr/bin/env python
# encoding: utf-8

import models

import requests

base_url = "https://justcoin.com/api/v1/markets"


class Justcoin(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {'btc_eur': 'BTCEUR',
                    'btc_nok': 'BTCNOK',
                    'btc_ltc': 'BTCLTC',
                    'btc_xrp': 'BTCXRP'}

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url, self._symbol, 'depth')
        resp = self._request('GET', url).json()

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
        url = "%s/" % base_url
        resp = self._request('GET', url).json()

        for market in requests.get(url).json():
            if market['id'] == self._symbol:
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
