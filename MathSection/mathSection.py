import math
from markupsafe import escape
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    strl = ""
    newline = "<br/>"
    with open("cryptoAPI.txt") as infile:
        lines = infile.readlines()
        for x in lines:
            if x.split()[0] == "Price":
                price = x.split()[1]
                strl+="Percent Change Today: "
                strl+=((percentChange(x.split()[1],x.split()[2])))+newline
                strl+="Change in Dollars Today: "
                strl+=((dollarChange(float(x.split()[1]),float(x.split()[2]))))+newline
            elif x.split()[0] == "Volume":
                strl+=" Average Volume: "
                strl+=((averageVolume(x.split()[1:len(x.split())])))+newline
            elif x.split()[0] == "Shares":
                shares = x.split()[1]
    strl+="Market Capitalization: "
    strl+=getMarketCap(int(shares),float(price))
            
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
        print("-")
        print(dec)
    else:
       dec = math.ceil((int((change)/10))%10*10 + change % 10)
       print("+")
       print(dec)
       print(change)
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
        return "{:0.2f}T".format(shares*currentPrice/1000000000000)
    if shares*currentPrice >= 1000000000:
        return "{:0.2f}B".format(shares*currentPrice/1000000000)
    return "{:0.2f}M".format(shares*currentPrice/1000000)
