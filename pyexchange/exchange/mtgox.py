#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models


class MtGox(models.Exchange):
    """Docstring for MtGox """
    _markets_map = {'btc_usd': 'BTCUSD',
                    'btc_gpb': 'BTCGPB',
                    'btc_eur': 'BTCEUR',
                    'btc_jpy': 'BTCJPY',
                    'btc_aud': 'BTCAUD',
                    'btc_cad': 'BTCCAD',
                    'btc_chf': 'BTCCHF',
                    'btc_cny': 'BTCCNY',
                    'btc_dkk': 'BTCDKK',
                    'btc_hkd': 'BTCHKD',
                    'btc_pln': 'BTCPLN',
                    'btc_rub': 'BTCRUB',
                    'btc_sek': 'BTCSEK',
                    'btc_sgd': 'BTCSGD',
                    'btc_thb': 'BTCTHB',
                    'btc_nok': 'BTCNOK',
                    'btc_czk': 'BTCCZK'}

    _endpoint = "http://data.mtgox.com/api/2/%(market)s/money/%(method)s"

    _api_methods = {'depth': {'method': 'GET',
                              'api': '/depth/fetch'},
                    'ticker': {'method': 'GET',
                               'api': '/ticker'},
                    'trades': {'method': 'GET',
                               'api': '/trades/fetch'}
                    }

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(MtGox, self)._create_request_methods(
                MtGox._endpoint,
                MtGox._api_methods)

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        resp = self._request_depth().json()
        resp = resp['data']
        asks = []
        for o in resp['asks']:
            asks.append(models.Order(price=o['price'],
                                     amount=o['amount']))
        bids = []
        for oi in resp['bids']:
            bids.append(models.Order(price=o['price'],
                                     amount=o['amount']))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        resp = self._request_ticker().json()
        resp = resp['data']
        return models.Ticker(avg=float(resp['avg']['value']),
                             buy=float(resp['buy']['value']),
                             high=float(resp['high']['value']),
                             last=float(resp['last']['value']),
                             low=float(resp['low']['value']),
                             sell=float(resp['sell']['value']),
                             vol=float(resp['vol']['value']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        resp = self._request_trades().json()
        resp = resp['data']
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
