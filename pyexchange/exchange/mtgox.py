#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

from pyexchange.exchange import models

base_url = "http://data.mtgox.com/api/2"


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

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url,
                            self._symbol,
                            'money/depth/fetch')

        resp = self._request('GET', url).json()
        resp = resp['data']
        asks = []
        for o in resp['asks']:
            asks.append(models.Order(price=self._create_decimal(o['price']),
                                     amount=self._create_decimal(o['amount'])))
        bids = []
        for oi in resp['bids']:
            bids.append(models.Order(price=self._create_decimal(o['price']),
                                     amount=self._create_decimal(o['amount'])))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url,
                            self._symbol,
                            'money/ticker')

        resp = self._request('GET', url).json()
        resp = resp['data']
        return models.Ticker(avg=self._create_decimal(resp['avg']['value']),
                             buy=self._create_decimal(resp['buy']['value']),
                             high=self._create_decimal(resp['high']['value']),
                             last=self._create_decimal(resp['last']['value']),
                             low=self._create_decimal(resp['low']['value']),
                             sell=self._create_decimal(resp['sell']['value']),
                             vol=self._create_decimal(resp['vol']['value']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url,
                            self._symbol,
                            'money/trades/fetch')

        resp = self._request('GET', url).json()
        resp = resp['data']
        trades = []
        for t in resp:
            date = datetime.fromtimestamp(t['date'])
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = int(t['tid'])
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
