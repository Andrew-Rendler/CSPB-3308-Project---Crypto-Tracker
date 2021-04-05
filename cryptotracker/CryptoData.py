import os

#from .CryptoCompareAPI import CryptoCompareAPI

import requests

million = 1000000
billion = 1000000000
trillion = 1000000000000
API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f"
URL_FRAGMENT = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=5"
url = URL_FRAGMENT + "&api_key=" + API_KEY;

class CryptoData:
    dataList = []
    currentPrice = 0
    previousClose = 0
    volumeList = []

    def __init__(self):
        res = requests.get(url)
        self.dataList = res.json()['Data']['Data']
        self.currentPrice = self.dataList[len(self.dataList)-1]['close']
        self.previousClose = self.dataList[len(self.dataList)-2]['close']
        for i in range(5):
            self.volumeList.append(self.dataList[i]['volumefrom'])

    def getDic(self):
        dic = {}
        dic["Price"] = self.currentPrice
        dic["Percent Change"] = self.percentChange()
        dic["Dollar Change"] = self.dollarChange()
        dic["Average Volume"] = self.averageVolume()
        return dic

    def getData(self):
        return self.dataList

    def getVolume(self):
        return self.volumeList

    def percentChange(self):
        change = (self.currentPrice - self.previousClose)/self.previousClose
        return "{:0.2f}%".format(change*100)

    def averageVolume(self):
        if len(self.volumeList):
            avg = sum(self.volumeList)/len(self.volumeList)
            return "{:0.2f}".format(avg)
        return 0

    def dollarChange(self):
        change = self.currentPrice-self.previousClose
        if change > 0:
            return "+{:0.2f}".format(change)
        return "{:0.2f}".format(change)

    def marketCap(self):
        mcap = 18655837.5*self.currentPrice
        if mcap >= trillion:
            return "{:0.3f}T".format(mcap/trillion)
        if mcap >= billion:
            return "{:0.3f}B".format(mcap/billion)
        return "{:0.3f}M".format(mcap/million)
