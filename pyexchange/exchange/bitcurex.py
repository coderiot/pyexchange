#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

data_url = "https://%(market)s.bitcurex.com/data/%(method)s"


class Bitcurex(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_pln': 'pln',
                    'btc_eur': 'eur'}

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todoo

        """
        url = data_url % {'market': self._symbol,
                          'method': 'orderbook.json'}
        resp = self._request('GET', url).json()

        asks = []
        for p, a in resp['asks']:
            asks.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))
        bids = []
        for p, a in resp['bids']:
            bids.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = data_url % {'market': self._symbol,
                          'method': 'ticker.json'}
        resp = self._request('GET', url).json()

        return models.Ticker(avg=self._create_decimal(resp['avg']),
                             buy=self._create_decimal(resp['buy']),
                             high=self._create_decimal(resp['high']),
                             last=self._create_decimal(resp['last']),
                             low=self._create_decimal(resp['low']),
                             sell=self._create_decimal(resp['sell']),
                             vol=self._create_decimal(resp['vol']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = data_url % {'market': self._symbol,
                          'method': 'trades.json'}
        resp = self._request('GET', url).json()

        trades = []
        for t in resp:
            date = datetime.fromtimestamp(t['date'])
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = t['tid']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
