import os
from .CryptoCompareAPI import CryptoCompareAPI

million = 1000000
billion = 1000000000
trillion = 1000000000000

class CryptoData:
    def __init__(self):
        self.dataList =[]
        self.currentPrice = 0
        self.previousClose = 0
        self.volumeList=[]

    def apiCall(self, kwargs):
        cryptocompare_api = CryptoCompareAPI()
        res = cryptocompare_api._api_call("historical_daily", kwargs)
        self.dataList = res.json()['Data']['Data']
        self.currentPrice = self.dataList[len(self.dataList)-1]['close']
        self.previousClose = self.dataList[len(self.dataList)-2]['close']
        for i in range(int(kwargs['num_days'])):
            self.volumeList.append(self.dataList[i]['volumefrom'])

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

