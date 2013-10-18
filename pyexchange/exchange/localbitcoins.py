#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

import requests

class LocalBitcoins(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {'btc_ars': 'ARS',
                    'btc_aud': 'AUD',
                    'btc_brl': 'BRL',
                    'btc_cad': 'CAD',
                    'btc_eur': 'EUR',
                    'btc_gbp': 'GBP',
                    'btc_ghs': 'GHS',
                    'btc_huf': 'HUF',
                    'btc_mxn': 'MXN',
                    'btc_nzd': 'NZD',
                    'btc_php': 'PHP',
                    'btc_pln': 'PLN',
                    'btc_rub': 'RUB',
                    'btc_sgd': 'SGD',
                    'btc_thb': 'THB',
                    'btc_usd': 'USD',
                    'btc_zar': 'ZAR'}

    _endpoint = "https://localbitcoins.com/bitcoincharts/%(market)s/%(method)s"

    _api_methods = {'depth': {'method': 'GET',
                              'api': 'orderbook.json'},
                    #'ticker': {'method': 'GET',
                               #'api': 'ticker'},
                    'trades': {'method': 'GET',
                               'api': 'trades.json'}
                    }

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(LocalBitcoins, self)._create_request_methods(
                LocalBitcoins._endpoint,
                LocalBitcoins._api_methods)

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
        m = self._markets_map[self.market]
        url = "https://localbitcoins.com/bitcoinaverage/ticker-all-currencies/"
        resp = requests.get(url).json()[m]
        return models.Ticker(avg=resp['avg_24h'],
                             buy=None,
                             high=None,
                             last=float(resp['rates']['last']),
                             low=None,
                             sell=None,
                             vol=float(resp['volume_btc']))

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
