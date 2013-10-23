#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://intersango.com/api"


class Intersango(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_gbp': 1,
                    'btc_eur': 2,
                    'btc_usd': 3,
                    'btc_pln': 4}

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s.php?currency_pair_id=%s" % (base_url,
                                                 'depth',
                                                 self._symbol)
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
        url = "%s/%s.php?currency_pair_id=%s" % (base_url,
                                                 'ticker',
                                                 self._symbol)
        resp = self._request('GET', url).json()
        return models.Ticker(avg=None,
                             buy=self._create_decimal(resp['buy']),
                             high=None,
                             last=self._create_decimal(resp['last']),
                             low=None,
                             sell=self._create_decimal(resp['sell']),
                             vol=self._create_decimal(resp['vol']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "%s/%s.php?currency_pair_id=%s" % (base_url,
                                                 'trades',
                                                 self._symbol)
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
