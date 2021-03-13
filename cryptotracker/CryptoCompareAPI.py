from flask import Flask, abort
import requests

API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f"

CRYPTOCOMPARE_ENDPOINTS = {
    "historical_daily": "https://min-api.cryptocompare.com/data/v2/histoday?fsym={coin}&&tsym={currency}&limit={num_days}"
}


class CryptoCompareAPI(object):
    def __init__(self):
        pass

    # endpoint, coin, currency, num_days
    def _url_builder(self, endpoint, **kwargs):
        url = CRYPTOCOMPARE_ENDPOINTS[endpoint].format(**kwargs)
        url += "&api_key={}".format(API_KEY)
        return url

    def _api_call(self, endpoint, kwargs):
        res = requests.get(self._url_builder(endpoint, **kwargs))
        return res
