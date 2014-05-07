#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

from pyexchange.exchange import models

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
            asks.append(models.Order(price=self._create_decimal(o['price']),
                                     amount=self._create_decimal(o['amount'])))
        bids = []
        for o in resp['bids']:
            bids.append(models.Order(price=self._create_decimal(o['price']),
                                     amount=self._create_decimal(o['amount'])))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "/".join([base_url, 'ticker', self._symbol])

        resp = self._request('GET', url).json()

        return models.Ticker(avg=self._create_decimal(resp['mid']),
                             buy=self._create_decimal(resp['bid']),
                             last=self._create_decimal(resp['last_price']),
                             sell=self._create_decimal(resp['ask']),
                             )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'trades', self._symbol])

        resp = self._request('GET', url).json()
        trades = []
        for t in resp:
            date = datetime.fromtimestamp(t['timestamp'])
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = None
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
