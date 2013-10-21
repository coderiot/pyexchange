#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://www.bitstamp.net/api/"

class Bitstamp(models.Exchange):
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
        url = "/".join([base_url, 'order_book'])
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
        url = "/".join([base_url, 'ticker'])
        resp = self._request('GET', url).json()

        return models.Ticker(avg=None,# high + low / 2.
                             high=float(resp['high']),
                             low=float(resp['low']),
                             last=float(resp['last']),
                             buy=float(resp['bid']),
                             sell=float(resp['ask']),
                             vol=float(resp['volume']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'transactions'])
        resp = self._request('GET', url).json()

        trades = []
        for t in resp:
            date = datetime.fromtimestamp(int(t['date']))
            amount = t['amount']
            price = t['price']
            tid = t['tid']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
