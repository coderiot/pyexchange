#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime
import hashlib
import hmac
import time

import models

base_url = "https://bter.com/api/1"


class Bter(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {"btc_cny": "btc_cny",
                    "ltc_cny": "ltc_cny",
                    "bqc_cny": "bqc_cny",
                    "btb_cny": "btb_cny",
                    "btr_cny": "btr_cny",
                    "cent_cny": "cent_cny",
                    "cmc_cny": "cmc_cny",
                    "cnc_cny": "cnc_cny",
                    "dgc_cny": "dgc_cny",
                    "doge_cny": "doge_cny",
                    "dtc_cny": "dtc_cny",
                    "dvc_cny": "dvc_cny",
                    "exc_cny": "exc_cny",
                    "ftc_cny": "ftc_cny",
                    "frc_cny": "frc_cny",
                    "ifc_cny": "ifc_cny",
                    "mec_cny": "mec_cny",
                    "mmc_cny": "mmc_cny",
                    "net_cny": "net_cny",
                    "nmc_cny": "nmc_cny",
                    "nxt_cny": "nxt_cny",
                    "ppc_cny": "ppc_cny",
                    "pts_cny": "pts_cny",
                    "qrk_cny": "qrk_cny",
                    "red_cny": "red_cny",
                    "src_cny": "src_cny",
                    "tag_cny": "tag_cny",
                    "tix_cny": "tix_cny",
                    "wdc_cny": "wdc_cny",
                    "xpm_cny": "xpm_cny",
                    "yac_cny": "yac_cny",
                    "zcc_cny": "zcc_cny",
                    "zet_cny": "zet_cny",
                    "ltc_btc": "ltc_btc",
                    "bqc_btc": "bqc_btc",
                    "btb_btc": "btb_btc",
                    "buk_btc": "buk_btc",
                    "cdc_btc": "cdc_btc",
                    "cmc_btc": "cmc_btc",
                    "cnc_btc": "cnc_btc",
                    "dgc_btc": "dgc_btc",
                    "doge_btc": "doge_btc",
                    "dtc_btc": "dtc_btc",
                    "exc_btc": "exc_btc",
                    "frc_btc": "frc_btc",
                    "ftc_btc": "ftc_btc",
                    "mec_btc": "mec_btc",
                    "mmc_btc": "mmc_btc",
                    "nec_btc": "nec_btc",
                    "nmc_btc": "nmc_btc",
                    "nxt_btc": "nxt_btc",
                    "ppc_btc": "ppc_btc",
                    "pts_btc": "pts_btc",
                    "qrk_btc": "qrk_btc",
                    "src_btc": "src_btc",
                    "tag_btc": "tag_btc",
                    "yac_btc": "yac_btc",
                    "wdc_btc": "wdc_btc",
                    "xpm_btc": "xpm_btc",
                    "zcc_btc": "zcc_btc",
                    "zet_btc": "zet_btc",
                    "bqc_ltc": "bqc_ltc",
                    "cent_ltc": "cent_ltc",
                    "cnc_ltc": "cnc_ltc",
                    "dvc_ltc": "dvc_ltc",
                    "ftc_ltc": "ftc_ltc",
                    "frc_ltc": "frc_ltc",
                    "ifc_ltc": "ifc_ltc",
                    "net_ltc": "net_ltc",
                    "nmc_ltc": "nmc_ltc",
                    "ppc_ltc": "ppc_ltc",
                    "red_ltc": "red_ltc",
                    "tix_ltc": "tix_ltc",
                    "trc_ltc": "trc_ltc",
                    "wdc_ltc": "wdc_ltc",
                    "yac_ltc": "yac_ltc",
                    }

    def __init__(self, market="ltc_btc", api_key=None, api_secret=None):
        """@todo: to be defined1

        :currency: @todo

        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.market = market

    def authenticate(self, api_key, api_secret):
        """
        @summary: Sets BTER API key and secret needed for private trading
                  API calls.

        @param api_key: BTer API Key
        @param api_secret: BTer API Secret

        @return: Nothing.
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def _generate_nonce(self):
        """
        @summary: Generate Nonce for signature.

        @return: Nonce
        """
        return "%i" % (time.time() * 1E6)

    #####
    ## Public API functions
    ###
    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "/".join([base_url, 'depth', self._symbol])
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
        url = "/".join([base_url, 'ticker', self._symbol])
        resp = self._request('GET', url).json()

        return models.Ticker(avg=self._create_decimal(resp['avg']),
                             high=self._create_decimal(resp['high']),
                             low=self._create_decimal(resp['low']),
                             last=self._create_decimal(resp['last']),
                             buy=self._create_decimal(resp['buy']),
                             sell=self._create_decimal(resp['sell']),
        )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'trade', self._symbol])
        resp = self._request('GET', url).json()

        trades = []
        for t in resp['data']:
            date = datetime.fromtimestamp(int(t['date']))
            amount = self._create_decimal(t['amount'])
            price = self._create_decimal(t['price'])
            tid = int(t['tid'])
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades

    def pairs(self):
        """
        @summary: Fetches supported market pairs (f.e. 'ltc_btc')

        @return: List containing all supported market pairs.
        """
        url = "/".join([base_url, 'pairs'])
        resp = self._request('GET', url).json()

        return resp

    #####
    ## Private API functions (API keys needed)
    ###
    def _query_private(self, method, params=None):
        """
        @summary: Performs query to private BTer API calls.
                  Request parameters are signed with API secret
                  and headers are set up accordingly.

        @param method: API method to call (f.e. getfunds).
        @param params: Dictionary containing all parameters for the
                       API query.

        @return: Server response
        """
        url = "/".join([base_url, 'private', str(method)])

        if params is None:
            params = {
                'nonce': self._generate_nonce()
            }
        else:
            params["nonce"] = self._generate_nonce()

        encoded_params = models.requests.models.RequestEncodingMixin()._encode_params(params)
        sign = hmac.new(self.api_secret, encoded_params, hashlib.sha512)

        headers = {
            'key': self.api_key,
            'sign': sign.hexdigest()
        }

        resp = self._request('POST', url, data=params, headers=headers).json()

        return resp

    def getfunds(self):
        """
        @summary: Get information about funds.

        @return: Returns two dictionaries of available as well as locked funds.
        """
        resp = self._query_private('getfunds')

        if "available_funds" in resp:
            available_funds = resp["available_funds"]
        else:
            available_funds = None

        if "locked_funds" in resp:
            locked_funds = resp["locked_funds"]
        else:
            locked_funds = None

        return [available_funds, locked_funds]

    def _placeorder(self, order_type, rate, amount, pair=None):
        """
        @summary: Order placement.

        @param pair: Currency pair (f.e. 'ltc_btc')
        @param order_type: Trading type ('SELL' or 'BUY')
        @param rate: Buy or sell rate (f.e. '0.023')
        @param amount: Buy or sell amount (f.e. '100')

        @return: Server response.
        """
        if pair is None:
            pair = str(self._market)

        params = {
            'pair': str(pair),
            'type': str(order_type),
            'rate': str(rate),
            'amount': str(amount)
        }
        resp = self._query_private('placeorder', params)

        return resp

    def buy(self, rate, amount, pair=None):
        return self._placeorder('BUY', rate, amount, pair)

    def sell(self, rate, amount, pair=None):
        return self._placeorder('SELL', rate, amount, pair)

    def cancelorder(self, order_id):
        """
        @summary: Cancel an order.

        @param order_id: Order ID (f.e. '123456')

        @return: Server response.

        """
        params = {
            'order_id': str(order_id)
        }

        resp = self._query_private('cancelorder', params)

        return resp

    def getorder(self, order_id):
        """
        @summary: Get detailed info about specific order.

        @param order_id: Order ID (f.e. '123456')

        @return: Order info.
        """
        params = {
            'order_id': str(order_id)
        }

        resp = self._query_private('getorder', params)

        if resp["msg"] == 'Success':
            order = resp["order"]

        return order

    def orderlist(self):
        """
        @summary: Get a list of active orders.

        @return: List of active orders.
        """
        resp = self._query_private('orderlist')

        if resp["msg"] == 'Success':
            orders = resp["orders"]

        return orders
