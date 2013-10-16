#!/usr/bin/env python
# encoding: utf-8

import models

import requests


class Campbx(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_usd': 'btc_usd'}

    _endpoint = "https://campbx.com/api/%(method)s"

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def book(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = Campbx._endpoint % {'method': 'xdepth.php'}
        resp = requests.get(url).json()

        asks = []
        for p, a in resp['Asks']:
            asks.append(models.Order(price=p,
                                     amount=a))
        bids = []
        for p, a in resp['Bids']:
            bids.append(models.Order(price=p,
                                     amount=a))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = Campbx._endpoint % {'method': 'xticker.php'}
        resp = requests.get(url).json()
        return models.Ticker(avg=None,# high + low / 2.
                             high=None,
                             low=None,
                             last=float(resp['Last Trade']),
                             buy=float(resp['Best Bid']),
                             sell=float(resp['Best Ask']),
                             vol=None)

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []
