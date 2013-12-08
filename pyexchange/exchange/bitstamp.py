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
        url = "/".join([base_url, 'ticker'])
        resp = self._request('GET', url).json()

        return models.Ticker(
                             high=self._create_decimal(resp['high']),
                             low=self._create_decimal(resp['low']),
                             last=self._create_decimal(resp['last']),
                             buy=self._create_decimal(resp['bid']),
                             sell=self._create_decimal(resp['ask']),
                             vol=self._create_decimal(resp['volume']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'transactions'])
        resp = self._request('GET', url).json()

        trades = []
        for t in resp:
            date = datetime.fromtimestamp(int(t['date']))
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = t['tid']
            trades.append(models.Trade(date=date,
                                       price=price,
                                       amount=amount,
                                       tid=tid))

        return trades
