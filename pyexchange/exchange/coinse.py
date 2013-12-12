#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime

import models

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

    def __init__(self, market="ltc_btc"):
        """@todo: to be defined1

        :currency: @todo

        """
        self.market = market

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
