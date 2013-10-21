#!/usr/bin/env python
# encoding: utf-8

import models

base_url = "https://campbx.com/api/"


class Campbx(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_usd': 'btc_usd'}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = base_url + "xdepth.php"
        resp = self._request("GET", url).json()

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
        #resp = self._request_ticker().json()
        url = base_url + "xticker.php"
        resp = self._request("GET", url).json()
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
