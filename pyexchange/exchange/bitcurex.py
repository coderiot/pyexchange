#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models


class Bitcurex(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_pln': 'pln',
                   'btc_eur': 'eur'}

    _api_methods = {'depth': {'method': 'GET',
                              'api': 'orderbook.json'},
                    'ticker': {'method': 'GET',
                               'api': 'ticker.json'},
                    'trades': {'method': 'GET',
                               'api': 'trades.json'}}

    _endpoint = "https://%(market)s.bitcurex.com/data/%(method)s"

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(Bitcurex, self)._create_request_methods(
                Bitcurex._endpoint,
                Bitcurex._api_methods)

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todoo

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
        resp = self._request_ticker()
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
        resp = self._request_trades()
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
