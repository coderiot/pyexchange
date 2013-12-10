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
            asks.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))
        bids = []
        for p, a in resp['Bids']:
            bids.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        #resp = self._request_ticker().json()
        url = base_url + "xticker.php"
        resp = self._request("GET", url).json()
        return models.Ticker(
                             last=self._create_decimal(resp['Last Trade']),
                             buy=self._create_decimal(resp['Best Bid']),
                             sell=self._create_decimal(resp['Best Ask']),
                             )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []
