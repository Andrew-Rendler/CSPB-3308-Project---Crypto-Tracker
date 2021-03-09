import math
import CryptoPriceData
from markupsafe import escape
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    strl = ""
    newline = "<br/>"
    price = CryptoPriceData.CryptoPriceData()
    price.getData('BTC','USD',0,2)
    strl+="Percent Change Today: "
    strl+=percentChange(price.priceList[0],price.priceList[1])+newline
    strl+="Change in Dollars Today: "
    strl+=dollarChange(price.priceList[0],price.priceList[1])+newline
    #will need volume data to display current or avg volume
    #hardcoded current # of 'coins' to get market cap
    strl+="Market Capitalization: "
    strl+=getMarketCap(18649443.75, price.priceList[0])+newline         
    return strl
    
def percentChange(currentPrice, prevPrice):
    return "{:0.2f}%".format((float(currentPrice)
                              -float(prevPrice))/float(prevPrice)*100)

def averageVolume(volList):
    if len(volList) > 0:
        volList = [int(i) for i in volList]
        return "{:0.2f}M".format(sum(volList)/len(volList)/1000000)
    return 0

def dollarChange(currentPrice, prevPrice):
    change = math.ceil((currentPrice*100) - (prevPrice*100))
    if change <= 0:
        dec = math.ceil((int((-1*change)/10))%10*10 + -1*change % 10)
    else:
       dec = math.ceil((int((change)/10))%10*10 + change % 10)
    if dec <= 9:
        dec = ("0"+str(int(dec)))
        if change >= 0:
            return "+{}.".format(int((change-int(dec))/100))+dec
        return "{}.".format(int((change+int(dec))/100))+dec
    elif change <= 0:
        return "{}.{}".format(int((change+dec)/100),int(dec))
    return "+{}.{}".format(int((change-dec)/100),int(dec))

def getMarketCap(shares, currentPrice):
    if shares*currentPrice >= 1000000000000:
        return "{:0.3f}T".format(shares*currentPrice/1000000000000)
    if shares*currentPrice >= 1000000000:
        return "{:0.3f}B".format(shares*currentPrice/1000000000)
    return "{:0.3f}M".format(shares*currentPrice/1000000)

