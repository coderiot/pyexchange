#!/usr/bin/env python
# encoding: utf-8

from pyexchange.exchange import models

base_url = "https://crypto-trade.com/api/1"


class Cryptotrade(models.Exchange):
    """Docstring for Cryptotrade"""

    _markets_map = {'btc_usd': 'btc_usd',
                    'btc_eur': 'btc_eur',
                    'ltc_usd': 'ltc_usd',
                    'ltc_eur': 'ltc_eur',
                    'ltc_btc': 'ltc_btc',
                    'nmc_usd': 'nmc_usd',
                    'nmc_btc': 'nmc_btc',
                    'xpm_usd': 'xpm_usd',
                    'xpm_btc': 'xpm_btc',
                    'xpm_ppc': 'xpm_ppc',
                    'ppc_usd': 'ppc_usd',
                    'ppc_btc': 'ppc_btc',
                    'trc_btc': 'trc_btc',
                    'ftc_usd': 'ftc_usd',
                    'ftc_btc': 'ftc_btc',
                    'dvc_btc': 'dvc_btc',
                    'wdc_btc': 'wdc_btc',
                    'wdc_usd': 'wdc_usd',
                    'dgc_btc': 'dgc_btc'}

    def __init__(self, market="btc_usd"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "%s/%s/%s" % (base_url, 'depth', self._symbol)
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
        url = "%s/%s/%s" % (base_url, 'ticker', self._symbol)
        resp = self._request('GET', url).json()

        return models.Ticker(
                             high=self._create_decimal(resp['data']['high']),
                             low=self._create_decimal(resp['data']['low']),
                             last=self._create_decimal(resp['data']['last']),
                             buy=self._create_decimal(resp['data']['max_bid']),
                             sell=self._create_decimal(resp['data']['min_ask']),
                             vol=self._create_decimal(resp['data']['vol_btc']))

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        return []


    def _hmac_request(self, url, params=None):
        return super(Cryptotrade, self)._hmac_request(url, params, key_name="AuthKey", sign_name="AuthSign")

    def get_balances(self):
        """
        @summary: Get information about funds.

        @return: Returns two dictionaries of available as well as locked funds.
        """
        url = "/".join([base_url, 'private', 'getinfo'])

        resp = self._hmac_request(url)

        if resp["status"] == 'success':
            funds = resp["data"]["funds"]

        return funds

    def _trade(self, order_type, rate, amount):
        """
        @summary: Order placement.

        @param order_type: Trading type ('Sell' or 'Buy')
        @param rate: Buy or sell rate (f.e. '0.023')
        @param amount: Buy or sell amount (f.e. '100')

        @return: Server response.
        """

        params = {
            'pair': self._symbol,
            'type': str(order_type),
            'rate': str(rate),
            'amount': str(amount)
        }

        url = "/".join([base_url, 'private', 'trade'])
        resp = self._hmac_request(url, params)

        return resp

    def buy(self, rate, amount):
        return self._neworder('Buy', rate, amount)

    def sell(self, rate, amount):
        return self._neworder('Sell', rate, amount)

    def cancel_order(self, order_id):
        """
        @summary: Cancel an order.

        @param order_id: Order ID (f.e. '123456')

        @return: Server response.

        """
        params = {
            'orderid': str(order_id),
        }

        url = "/".join([base_url, 'private', 'cancelorder'])
        resp = self._hmac_request(url, params)

        return resp

    def get_order_status(self, order_id):
        """
        @summary: Get detailed info about specific order.

        @param order_id: Order ID (f.e. '123456')

        @return: Order info.
        """
        params = {
            'orderid': str(order_id),
        }

        url = "/".join([base_url, 'private', 'orderinfo'])
        resp = self._hmac_request(url, params)

        if resp["status"] == 'success':
            order = resp["data"]

        return order
