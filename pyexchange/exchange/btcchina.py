#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://btcchina.com"


class BtcChina(models.Exchange):
    _markets_map = {'btc_cny': 'btc_cny'}

    def __init__(self, market="btc_cny"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s" % (base_url, 'bc/orderbook')
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
        url = "%s/%s" % (base_url, 'bc/ticker')
        resp = self._request('GET', url).json()
        resp = resp['ticker']

        return models.Ticker(
                             high=self._create_decimal(resp['high']),
                             low=self._create_decimal(resp['low']),
                             last=self._create_decimal(resp['last']),
                             buy=self._create_decimal(resp['buy']),
                             sell=self._create_decimal(resp['sell']),
                             vol=self._create_decimal(resp['vol']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "%s/%s" % (base_url, 'bc/trades')
        resp = self._request('GET', url).json()

        trades = []
        for t in resp:
            date = datetime.fromtimestamp(int(t['date']))
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = int(t['tid'])
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
