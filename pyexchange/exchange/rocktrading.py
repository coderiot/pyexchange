#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models


base_url = "https://www.therocktrading.com/api"


class RockTrading(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_eur': 'BTCEUR',
                    'btc_usd': 'BTCUSD',
                    'btc_xrp': 'BTCXRP',
                    'eur_xrp': 'EURXRP',
                    'ltc_btc': 'LTCBTC',
                    'ltc_eur': 'LTCEUR'}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url, 'orderbook', self._symbol)
        resp = self._request('GET', url, verify=False).json()

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
        url = "%s/%s/%s" % (base_url, 'ticker', self._symbol)
        resp = self._request('GET', url, verify=False).json()
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
        url = "%s/%s/%s" % (base_url, 'trades', self._symbol)
        resp = self._request('GET', url, verify=False).json()

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
