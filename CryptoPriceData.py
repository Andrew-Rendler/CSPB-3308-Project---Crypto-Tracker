from flask import Flask, abort
import requests

API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f"

class CryptoPriceData:

    def __init__(self):
        self.priceList = []

    def getData(self, coin, cur, daysAgo, history):
        price = get_price.get_price(coin, cur, daysAgo, history)
        for i in range(len(price)):
            self.priceList.append(price[i][coin][cur])

    #we should construct our own urls and pass the arguments as needed to the api
    def get_daily(self, crypto, currency, num_days):
        request = requests.get('https://min-api.cryptocompare.com/data/v2/histoday?fsym='+ str(crypto) + '&tsym=' + str(currency) + '&limit=' + str(num_days) + "&api_key=" + API_KEY)
        return request

    def api_call(self):
        print(requests.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=10&api_key=15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f%27"))
