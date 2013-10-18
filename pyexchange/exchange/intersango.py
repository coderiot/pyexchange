#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models


class Intersango(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_gbp': 1,
                    'btc_eur': 2,
                    'btc_usd': 3,
                    'btc_pln': 4}

    _endpoint = "https://intersango.com/api/%(method)s.php?currency_pair_id=%(market)d"

    _api_methods = {'depth': {'method': 'GET',
                              'api': 'depth'},
                    'ticker': {'method': 'GET',
                               'api': 'ticker'},
                    'trades': {'method': 'GET',
                               'api': 'trades'}
                    }

    def __init__(self, market="btc_eur"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(Intersango, self)._create_request_methods(
                Intersango._endpoint,
                Intersango._api_methods)

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
        return models.Ticker(avg=None,
                             buy=float(resp['buy']),
                             high=None,
                             last=float(resp['last']),
                             low=None,
                             sell=float(resp['sell']),
                             vol=float(resp['vol']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        resp = self._request_trades().json()
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
