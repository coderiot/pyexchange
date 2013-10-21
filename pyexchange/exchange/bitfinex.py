#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://api.bitfinex.com/v1"


class Bitfinex(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_usd': 'btcusd',
                    'ltc_usd': 'ltcusd',
                    'ltc_btc': 'ltcbtc'}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "/".join([base_url, 'book', self._symbol])

        resp = self._request('GET', url).json()

        asks = []
        for o in resp['asks']:
            asks.append(models.Order(price=o['price'],
                                     amount=o['amount']))
        bids = []
        for o in resp['bids']:
            bids.append(models.Order(price=o['price'],
                                     amount=o['amount']))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "/".join([base_url, 'ticker', self._symbol])

        resp = self._request('GET', url).json()

        return models.Ticker(avg=float(resp['mid']),
                             buy=float(resp['bid']),
                             high=None,
                             last=float(resp['last_price']),
                             low=None,
                             sell=float(resp['ask']),
                             vol=None)

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'trades', self._symbol])

        resp = self._request('GET', url).json()
        trades = []
        for t in resp:
            date = datetime.fromtimestamp(t['timestamp'])
            amount = t['amount']
            price = t['price']
            tid = None
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
