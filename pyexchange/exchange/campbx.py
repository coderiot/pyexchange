#!/usr/bin/env python
# encoding: utf-8

import models


class Campbx(models.Exchange):
    """Docstring for Bitstamp """

    _markets_map = {'btc_usd': 'btc_usd'}

    _endpoint = "https://campbx.com/api/%(method)s"

    _api_methods = {'depth': {'method': 'GET',
                              'api': 'xdepth.php'},
                    'ticker': {'method': 'GET',
                               'api': 'xticker.php'},
                    #'trades': {'method': 'GET',
                               #'api': 'trades'}
                    }

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        super(Campbx, self)._create_request_methods(
                Campbx._endpoint,
                Campbx._api_methods)

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        resp = self._request_depth().json()

        asks = []
        for p, a in resp['Asks']:
            asks.append(models.Order(price=p,
                                     amount=a))
        bids = []
        for p, a in resp['Bids']:
            bids.append(models.Order(price=p,
                                     amount=a))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        resp = self._request_ticker().json()
        return models.Ticker(avg=None,# high + low / 2.
                             high=None,
                             low=None,
                             last=float(resp['Last Trade']),
                             buy=float(resp['Best Bid']),
                             sell=float(resp['Best Ask']),
                             vol=None)

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []
