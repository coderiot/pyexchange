#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models


class Bitstamp(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {'btc_usd': 'btc_usd'}

    _endpoint = "https://www.bitstamp.net/api/%(method)s/"

    _api_methods = {'depth': {'method': 'GET',
                              'api': 'order_book'},
                    'ticker': {'method': 'GET',
                               'api': 'ticker'},
                    'trades': {'method': 'GET',
                               'api': 'transactions'}}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(Bitstamp, self)._create_request_methods(
                Bitstamp._endpoint,
                Bitstamp._api_methods)

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        resp = self._request_depth().json()

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
        resp = self._request_ticker().json()
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
        resp = self._request_trades().json()
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
