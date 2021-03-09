import get_price

class CryptoPriceData:
    
    def __init__(self):
        self.priceList = []

    def getData(self, coin, cur, daysAgo, history):
        price = get_price.get_price(coin, cur, daysAgo, history)
        for i in range(len(price)):
            self.priceList.append(price[i][coin][cur])
            
        
