#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

base_url = "https://btc-e.com/api/2"

class Btce(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {'btc_usd': 'btc_usd',
                    'btc_eur': 'btc_eur',
                    'btc_rur': 'btc_rur',
                    'ltc_btc': 'ltc_btc',
                    'ltc_usd': 'ltc_usd',
                    'ltc_rur': 'ltc_rur',
                    'ltc_eur': 'ltc_eur',
                    'nmc_btc': 'nmc_btc',
                    'nmc_usd': 'nmc_bsd',
                    'nvc_btc': 'nvc_btc',
                    'nvc_usd': 'nvc_usd',
                    'usd_rur': 'usd_rur',
                    'eur_usd': 'eur_usd',
                    'trc_btc': 'trc_btc',
                    'ppc_btc': 'ppc_btc',
                    'ftc_btc': 'ftc_btc'}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "/".join([base_url, self._symbol, 'depth'])
        resp = self._request('GET', url).json()

        asks = []
        for p, a in resp['asks']:
            asks.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))
        bids = []
        for p, a in resp['bids']:
            bids.append(models.Order(price=self._create_decimal(p),
                                     amount=self._create_decimal(a)))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "/".join([base_url, self._symbol, 'ticker'])
        resp = self._request('GET', url).json()

        return models.Ticker(avg=self._create_decimal(resp['ticker']['avg']),
                      high=self._create_decimal(resp['ticker']['high']),
                      low=self._create_decimal(resp['ticker']['low']),
                      last=self._create_decimal(resp['ticker']['last']),
                      buy=self._create_decimal(resp['ticker']['buy']),
                      sell=self._create_decimal(resp['ticker']['sell']),
                      vol=self._create_decimal(resp['ticker']['vol'])
                      )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, self._symbol, 'trades'])
        resp = self._request('GET', url).json()

        trades = []
        for t in resp:
            date = datetime.fromtimestamp(int(t['date']))
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = t['tid']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
