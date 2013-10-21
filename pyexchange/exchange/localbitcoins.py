#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

data_url = "https://localbitcoins.com"

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


    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s/%s/%s" % (data_url,
                               'bitcoincharts',
                               self._symbol,
                               'orderbook.json')

        resp = self._request('GET', url).json()

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
        url = "%s/%s" % (data_url,
                        'bitcoinaverage/ticker-all-currencies')

        resp = self._request('GET', url).json()
        resp = resp[self._symbol]

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
        url = "%s/%s/%s/%s" % (data_url,
                               'bitcoincharts',
                               self._symbol,
                               'trades.json')

        resp = self._request('GET', url).json()

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
