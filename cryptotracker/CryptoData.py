try:
    from CryptoCompareAPI import CryptoCompareAPI
except:
    from .CryptoCompareAPI import CryptoCompareAPI

MILLION = 1000000
BILLION = 1000000000
TRILLION = 1000000000000
NUM_ENTRIES = 5


class CryptoData:
    dataList = []
    currentPrice = 0
    previousClose = 0
    volumeList = []

    def __init__(self):
        cc_api = CryptoCompareAPI()
        payload = {"coin": "BTC", "currency": "USD", "num_entries": NUM_ENTRIES}
        res = cc_api.api_call("historical+daily", payload)
        self.dataList = res.json()["Data"]["Data"]
        self.currentPrice = self.dataList[len(self.dataList) - 1]["close"]
        self.previousClose = self.dataList[len(self.dataList) - 2]["close"]
        for i in range(NUM_ENTRIES):
            self.volumeList.append(self.dataList[i]["volumefrom"])

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
        change = (self.currentPrice - self.previousClose) / self.previousClose
        return "{:0.2f}%".format(change * 100)

    def averageVolume(self):
        if len(self.volumeList):
            avg = sum(self.volumeList) / len(self.volumeList)
            return "{:0.2f}".format(avg)
        return 0

    def dollarChange(self):
        change = self.currentPrice - self.previousClose
        if change > 0:
            return "+{:0.2f}".format(change)
        return "{:0.2f}".format(change)

    def marketCap(self):
        mcap = 18655837.5 * self.currentPrice
        if mcap >= TRILLION:
            return "{:0.3f}T".format(mcap / TRILLION)
        if mcap >= BILLION:
            return "{:0.3f}B".format(mcap / BILLION)
        return "{:0.3f}M".format(mcap / MILLION)
