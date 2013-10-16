#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

import requests


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

    _endpoint = "https://btc-e.com/api/2/%(market)s/%(method)s"

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = Btce._endpoint % {'market': self.market, 'method': 'depth'}
        resp = requests.get(url).json()

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
        url = Btce._endpoint % {'market': self.market, 'method': 'ticker'}
        j = requests.get(url).json()
        r = j['ticker']
        return models.Ticker(avg=r['avg'],
                      high=r['high'],
                      low=r['low'],
                      last=r['last'],
                      buy=r['buy'],
                      sell=r['sell'],
                      vol=r['vol']
                      )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = Btce._endpoint % {'market': self.market, 'method': 'trades'}
        resp = requests.get(url).json()
        trades = []
        for t in resp:
            date = datetime.fromtimestamp(int(t['date']))
            amount = t['amount']
            price = t['price']
            tid = t['tid']
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades
