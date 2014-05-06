#!/usr/bin/env python
# encoding: utf-8

from pyexchange.exchange import models

from pyexchange.exchange import *


def exchanges():
    """List names of available exchanges.
    :returns: list of strings

    supported exchanges:

    ['localbitcoins',
     'mtgox',
     'therock',
     'bitfinex',
     'cryptotrade',
     'bitstamp',
     'intersango',
     'campbx',
     'btce',
     'justcoin',
     'bitcurex']

    """
    return sorted([name for name in models.Exchange._register])


def new_exchange(name, market=None):
    """Create exchange object by name of the exchange.

    :name: name for the exchange
    :market: (optional) name of market for exchange creation
    :returns: exchange object

    """
    if name.lower() not in models.Exchange._register:
        raise Exception("Unknown Exchange name. \
                        Use pyexchange.exchanges for \
                        a list of all available Exchanges.")

    cls = models.Exchange._register[name.lower()]

    if market:
        obj = cls(market)
    else:
        obj = cls()
    return obj


def markets(name):
    """List markets for exchange.

    :name: the name of the exchange you want to know the
           available markets.
    :returns: List of markets. For example:

              ['btc_eur', 'btc_pln']

    """
    if name.lower() not in models.Exchange._register:
        raise Exception("Unknown Exchange name. \
                        Use pyexchange.exchanges for \
                        a list of all available Exchanges.")

    cls = models.Exchange._register[name.lower()]

    return cls().markets()


def find_market(market):
    """Find market on exchange by currency pair.

    :market: a string representing the market. (example: btc_usd)
    :returns: A list of tuples contain exchange name and market.
              For example:

              [('mtgox', 'btc_nok'), ('justcoin', 'btc_nok')]

    """
    markets = []
    for name, cls in models.Exchange._register.items():
        if market in cls._markets_map:
            markets.append((name, market))

    return markets
