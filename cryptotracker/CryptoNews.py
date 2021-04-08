try:
    from CryptoCompareAPI import CryptoCompareAPI
except:
    from .CryptoCompareAPI import CryptoCompareAPI  



class CryptoNews:
    newsList = []

    def __init__(self):
        cc_api = CryptoCompareAPI()
        res = cc_api.api_call("news+latest_news+articles",{})
        self.newsList = res.json()
        self.newsTitle = self.newsList[len(self.newsList) - 1]["title"]
        self.newsURL = self.newsList[len(self.newsList) - 1]["url"]
        
    def getDic(self):
        dic = {}
        dic["Title"] = self.currentTitle
        dic["Link"] = self.newsURL
        return dic

    def getData():
        cc_api = CryptoCompareAPI()
        passit = {}
        res = cc_api.api_call("news+latest_news+articles",{})
        newsList = res.json()
        newsURL1 = newsList["Data"][1]["url"]
        newsTitle1 = newsList["Data"][1]["title"]
        newsURL2 = newsList["Data"][2]["url"]
        newsTitle2 = newsList["Data"][2]["title"]
        newsURL3 = newsList["Data"][3]["url"]
        newsTitle3 = newsList["Data"][3]["title"]
        newsURL4 = newsList["Data"][4]["url"]
        newsTitle4 = newsList["Data"][4]["title"]
        newsURL5 = newsList["Data"][5]["url"]
        newsTitle5 = newsList["Data"][5]["title"]
        passit["URL1"] = newsURL1
        passit["title1"] = newsTitle1
        passit["URL2"] = newsURL2
        passit["title2"] = newsTitle2
        passit["URL3"] = newsURL3
        passit["title3"] = newsTitle3
        passit["URL4"] = newsURL4
        passit["title4"] = newsTitle4
        passit["URL5"] = newsURL5
        passit["title5"] = newsTitle5
        return passit
