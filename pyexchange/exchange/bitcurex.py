#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

import requests


class Bitcurex(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_pln': 'pln',
                   'btc_eur': 'eur'}

    _endpoint = "https://%(market)s.bitcurex.com/data/%(method)s"

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todoo

        """
        m = self._markets_map[self.market]
        url = Bitcurex._endpoint % {'market': m, 'method': 'orderbook.json'}

        resp = requests.get(url).json()
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
        m = self._markets_map[self.market]
        url = Bitcurex._endpoint % {'market': m, 'method': 'ticker.json'}
        resp = requests.get(url).json()
        return models.Ticker(avg=resp['avg'],
                             buy=resp['buy'],
                             high=resp['high'],
                             last=resp['last'],
                             low=resp['low'],
                             sell=resp['sell'],
                             vol=resp['vol'])

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        m = self._markets_map[self.market]
        url = Bitcurex._endpoint % {'market': m, 'method': 'trades.json'}
        resp = requests.get(url).json()
        trades = []
        for t in resp:
            date = datetime.fromtimestamp(t['date'])
            amount = t['amount']
            price = t['price']
            tid = t['tid']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
