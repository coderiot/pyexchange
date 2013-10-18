#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models


class RockTrading(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_eur': 'BTCEUR',
                    'btc_usd': 'BTCUSD',
                    'btc_xrp': 'BTCXRP',
                    'eur_xrp': 'EURXRP',
                    'ltc_btc': 'LTCBTC',
                    'ltc_eur': 'LTCEUR'}

    _endpoint = "https://www.therocktrading.com/api/%(method)s/%(market)s"

    _api_methods = {'depth': {'method': 'GET',
                              'api': 'orderbook'},
                    'ticker': {'method': 'GET',
                               'api': 'ticker'},
                    'trades': {'method': 'GET',
                               'api': 'trades'}
                    }

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(RockTrading, self)._create_request_methods(
                RockTrading._endpoint,
                RockTrading._api_methods)

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        resp = self._request_depth(verify=False).json()

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
        resp = self._request_ticker(verify=False).json()
        resp = resp['result'][0]

        return models.Ticker(avg=None,
                             buy=float(resp['bid']),
                             high=None,
                             last=None,
                             low=None,
                             sell=float(resp['ask']),
                             vol=None)

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        resp = self._request_trades(verify=False).json()
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
