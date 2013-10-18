#!/usr/bin/env python
# encoding: utf-8

from collections import namedtuple

import sys

import requests


class ExchangeMeta(type):
    """Metaclass for creating exchange objects.
    Add the subclass to an internal list to list exchanges.
    Also add markets() function to the module containing the class
    that list the markets of the exchange.
    """

    def __init__(cls, name, bases, dct):
        if not hasattr(cls, '_register'):
            cls._register = {}
        else:
            cls._register[name.lower()] = cls

        # add module.markets() function to list the
        # markets of the exchange representing by the module
        current_module = sys.modules[cls.__module__]
        current_module.markets = lambda: cls._markets_map.keys()
        super(ExchangeMeta, cls).__init__(name, bases, dct)


class Exchange(object):
    """Exchange Interface"""
    __metaclass__ = ExchangeMeta

    def _create_request_methods(self, endpoint, methods):
        """@todo: Docstring for __init__
        :returns: @todo

        """
        for m, d in methods.items():
            def _fn_handler(method=d['method'], api=d['api'], **args):
                market = self._markets_map[self.market]
                url = endpoint % {'market': market,
                                  'method': api}
                return requests.request(method, url, **args)

            setattr(self, '_request_%s' % m, _fn_handler)

    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, market):
        if market in self.__class__._markets_map:
            self._market = market
        else:
            raise Exception('Market not available for this Exchange.')

    def markets(self):
        """List the markets of the exchange

        :returns: list of strings. For example:

              ['btc_eur', 'btc_pln']

        """
        return self.__class__._markets_map.keys()


Ticker = namedtuple("Ticker", ["avg",
                               "high",
                               "low",
                               "last",
                               "buy",
                               "sell",
                               "vol"])

Trade = namedtuple("Trade", ["date",
                             "price",
                             "amount",
                             "tid"])

Order = namedtuple("Order", ["price",
                             "amount"])
