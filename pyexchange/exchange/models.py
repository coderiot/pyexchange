#!/usr/bin/env python
# encoding: utf-8

from collections import namedtuple
import decimal
import sys
import time

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
    decimal.setcontext(decimal.ExtendedContext)

    def __repr__(self):
        """@todo: Docstring for __repr__

        :arg1: @todo
        :returns: @todo

        """
        return "%s('%s')" % (self.__class__.__name__, self.market)

    def _create_decimal(self, dec_str):
        """@todo: Docstring for _create_decimal

        :str: @todo
        :returns: @todo

        """
        return decimal.getcontext().create_decimal(dec_str or 'NaN')

    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, market):
        cls = type(self)
        if market in cls._markets_map:
            self._market = market
            self._symbol = cls._markets_map[market]
        else:
            raise Exception('Market not available for this Exchange.')

    def markets(self):
        """List the markets of the exchange

        :returns: list of strings. For example:

              ['btc_eur', 'btc_pln']

        """
        return self.__class__._markets_map.keys()

    def _request(self, *args, **kwargs):
        """@todo: Docstring for request

        :*args: @todo
        :**kwargs: @todo
        :returns: @todo

        """

        return requests.request(*args, **kwargs)

    def _generate_nonce(self):
        """
        @summary: Generate Nonce for signature.

        @return: Nonce
        """
        return "%i" % (time.time() * 1E6)


TickerT = namedtuple("Ticker", ["avg",
                               "high",
                               "low",
                               "last",
                               "buy",
                               "sell",
                               "vol"])


class Ticker(TickerT):
    def __new__(cls, avg=decimal.Decimal('nan'),
                     high=decimal.Decimal('nan'),
                     low=decimal.Decimal('nan'),
                     last=decimal.Decimal('nan'),
                     buy=decimal.Decimal('nan'),
                     sell=decimal.Decimal('nan'),
                     vol=decimal.Decimal('nan'),
                     ):
        return super(Ticker, cls).__new__(cls, avg, high, low, last, buy, sell, vol)


Trade = namedtuple("Trade", ["date",
                             "price",
                             "amount",
                             "tid"])

Order = namedtuple("Order", ["price",
                             "amount"])
