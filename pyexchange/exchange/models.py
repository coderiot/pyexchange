#!/usr/bin/env python
# encoding: utf-8

from collections import namedtuple
import decimal
import hmac
import hashlib
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
            # called by Exchange super class
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

    def _hmac_request(self, url, params=None, key_name="key", sign_name="sign", hash_fun=hashlib.sha512):
        """
        @summary: Performs query to private BTer API calls.
                  Request parameters are signed with API secret
                  and headers are set up accordingly.

        @param method: API method to call (f.e. getfunds).
        @param params: Dictionary containing all parameters for the
                       API query.
        @param key_name: Name for api key in header. Default: key
        @param sign_name: Name for signed message in header. Default: sign
        @param hash_fun: Hash function for signing request. Default: hashlib.sha512

        @return: Server response
        """
        if params is None:
            params = {'nonce': self._generate_nonce()}
        else:
            params["nonce"] = self._generate_nonce()

        encoded_params = requests.models.RequestEncodingMixin()._encode_params(params)
        sign = hmac.new(self.api_secret, encoded_params, hash_fun)

        # TODO: header names will change for different apis
        headers = {
            key_name: self.api_key,
            sign_name: sign.hexdigest()
        }

        resp = self._request('POST', url, data=params, headers=headers).json()

        return resp

# wrapping Exchange class for python2 and 3 compatibility
Exchange = ExchangeMeta('Exchange', (Exchange, ), {})

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
