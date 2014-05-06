#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

from pyexchange.exchange import models

base_url = "https://www.coins-e.com/api/v2"


class Coinse(models.Exchange):
    """Docstring for Bitstamp """
    _markets_map = {
            "alp_btc": "ALP_BTC",
            "alp_ltc": "ALP_LTC",
            "amc_btc": "AMC_BTC",
            "amc_ltc": "AMC_LTC",
            "anc_btc": "ANC_BTC",
            "anc_ltc": "ANC_LTC",
            "arg_btc": "ARG_BTC",
            "arg_ltc": "ARG_LTC",
            "bet_btc": "BET_BTC",
            "bet_ltc": "BET_LTC",
            "bqc_btc": "BQC_BTC",
            "btg_btc": "BTG_BTC",
            "cgb_btc": "CGB_BTC",
            "cin_btc": "CIN_BTC",
            "cmc_btc": "CMC_BTC",
            "col_ltc": "COL_LTC",
            "crc_btc": "CRC_BTC",
            "csc_btc": "CSC_BTC",
            "dem_btc": "DEM_BTC",
            "dem_ltc": "DEM_LTC",
            "dgc_btc": "DGC_BTC",
            "dmd_btc": "DMD_BTC",
            "dtc_btc": "DTC_BTC",
            "elc_btc": "ELC_BTC",
            "elp_btc": "ELP_BTC",
            "emd_btc": "EMD_BTC",
            "ezc_btc": "EZC_BTC",
            "flo_btc": "FLO_BTC",
            "frk_btc": "FRK_BTC",
            "frk_ltc": "FRK_LTC",
            "ftc_btc": "FTC_BTC",
            "gdc_btc": "GDC_BTC",
            "glc_btc": "GLC_BTC",
            "glc_ltc": "GLC_LTC",
            "glx_btc": "GLX_BTC",
            "hyc_btc": "HYC_BTC",
            "ifc_btc": "IFC_BTC",
            "ifc_ltc": "IFC_LTC",
            "ifc_xpm": "IFC_XPM",
            "kgc_btc": "KGC_BTC",
            "kgc_ltc": "KGC_LTC",
            "lbw_btc": "LBW_BTC",
            "ltc_btc": "LTC_BTC",
            "mec_btc": "MEC_BTC",
            "nan_btc": "NAN_BTC",
            "net_btc": "NET_BTC",
            "nib_btc": "NIB_BTC",
            "nrb_btc": "NRB_BTC",
            "nuc_btc": "NUC_BTC",
            "nvc_btc": "NVC_BTC",
            "orb_btc": "ORB_BTC",
            "orb_ltc": "ORB_LTC",
            "ppc_btc": "PPC_BTC",
            "ppc_xpm": "PPC_XPM",
            "pts_btc": "PTS_BTC",
            "pwc_btc": "PWC_BTC",
            "pxc_btc": "PXC_BTC",
            "pxc_ltc": "PXC_LTC",
            "qrk_btc": "QRK_BTC",
            "qrk_ltc": "QRK_LTC",
            "qrk_xpm": "QRK_XPM",
            "rch_btc": "RCH_BTC",
            "rch_ltc": "RCH_LTC",
            "rec_btc": "REC_BTC",
            "rec_ltc": "REC_LTC",
            "red_btc": "RED_BTC",
            "red_ltc": "RED_LTC",
            "sbc_btc": "SBC_BTC",
            "sbc_ltc": "SBC_LTC",
            "spt_btc": "SPT_BTC",
            "tag_btc": "TAG_BTC",
            "trc_btc": "TRC_BTC",
            "uno_btc": "UNO_BTC",
            "vlc_btc": "VLC_BTC",
            "vlc_ltc": "VLC_LTC",
            "wdc_btc": "WDC_BTC",
            "xnc_btc": "XNC_BTC",
            "xnc_ltc": "XNC_LTC",
            "xpm_btc": "XPM_BTC",
            "xpm_ltc": "XPM_LTC",
            "zet_btc": "ZET_BTC"
            }

    def __init__(self, market="ltc_btc", api_key=None, api_secret=None):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market
        self.api_key = api_key
        self.api_secret = api_secret

    def depth(self):
        """@todo: Docstring for depth
        :returns: @todo

        """
        url = "/".join([base_url, 'market', self._symbol, 'depth/'])
        resp = self._request('GET', url).json()

        asks = []
        for o in resp['marketdepth']['asks']:
            asks.append(models.Order(price=self._create_decimal(o['r']),
                                     amount=self._create_decimal(o['q'])))
        bids = []
        for o in resp['marketdepth']['bids']:
            bids.append(models.Order(price=self._create_decimal(o['r']),
                                     amount=self._create_decimal(o['q'])))

        return asks, bids

    def ticker(self):
        """@todo: Docstring for ticker
        :returns: @todo

        """
        url = "/".join([base_url, 'markets/data/'])
        resp = self._request('GET', url).json()
        resp = resp['markets'][self._symbol]['marketstat']

        return models.Ticker(avg=self._create_decimal(resp['24h']['avg_rate']),
                      high=self._create_decimal(resp['24h']['h']),
                      low=self._create_decimal(resp['24h']['l']),
                      last=self._create_decimal(resp['ltp']),
                      buy=self._create_decimal(resp['bid']),
                      sell=self._create_decimal(resp['ask']),
                      vol=self._create_decimal(resp['24h']['volume']),
                      )

    def trades(self):
        """@todo: Docstring for trades
        :returns: @todo

        """
        url = "/".join([base_url, 'market', self._symbol, 'trades/'])
        resp = self._request('GET', url).json()

        trades = []
        for t in resp['trades']:
            date = datetime.fromtimestamp(int(t['created']))
            amount = self._create_decimal(t['quantity'])
            price = self._create_decimal(t['rate'])
            tid = None
            trades.append(models.Trade(date=date,
                                       amount=amount,
                                       price=price,
                                       tid=tid))

        return trades

    def _neworder(self, order_type, rate, amount):
        """
        @summary: Order placement.

        @param order_type: Trading type ('sell' or 'buy')
        @param rate: Buy or sell rate (f.e. '0.023')
        @param amount: Buy or sell amount (f.e. '100')

        @return: Server response.
        """

        params = {
            'method': 'neworder',
            'order_type': str(order_type),
            'rate': str(rate),
            'quantity': str(amount)
        }
        url = "/".join([base_url, 'market', self._symbol])
        resp = self._hmac_request(url, params)

        return resp

    def buy(self, rate, amount):
        return self._neworder('buy', rate, amount)

    def sell(self, rate, amount):
        return self._neworder('sell', rate, amount)

    def list_orders(self):
        """
        @summary: Get a list of active orders.

        @return: List of active orders.
        """
        url = "/".join([base_url, 'market', self._symbol])
        params = {'method': 'listorders'}
        resp = self._hmac_request(url, params)

        if resp["message"] == 'success':
            orders = resp["orders"]

        return orders

    def cancel_order(self, order_id):
        """
        @summary: Cancel an order.

        @param order_id: Order ID (f.e. '123456')

        @return: Server response.

        """
        params = {
            'order_id': str(order_id),
            'method': 'cancelorder'
        }

        url = "/".join([base_url, 'market', self._symbol])
        resp = self._hmac_request(url, params)

        if resp["message"] == 'success':
            order = resp["order"]

        return order

    def get_order_status(self, order_id):
        """
        @summary: Get detailed info about specific order.

        @param order_id: Order ID (f.e. '123456')

        @return: Order info.
        """
        params = {
            'order_id': str(order_id),
            'method': 'getorder'
        }

        url = "/".join([base_url, 'market', self._symbol])
        resp = self._hmac_request(url, params)

        if resp["message"] == 'success':
            order = resp["order"]

        return order
