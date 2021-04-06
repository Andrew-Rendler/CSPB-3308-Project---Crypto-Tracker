var ctx = document.getElementById('myChart');
var API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f";
var INTERVAL = 100
var URL_FRAGMENT = `https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=${INTERVAL}`;
var url = URL_FRAGMENT + "&api_key=" + API_KEY;
var T = 1000000000000;
var priceList = [];
var dates = [];

class ChartBuilder {
  constructor(interval) {
    this.priceList = []
    this.dates = []
    this.cryDataDay = []
    this.interval = interval;
    this.ctx = document.getElementById('chart').getContext('2d')
    this.ctx.canvas.width = 1000;
    this.ctx.canvas.height = 250;
  }

  fetchData(url) {
    return fetch(url).then(res => {
      return res.json()
    })
  }

  percentChange(num1, num2) {
    return (num1 - num2) / num2 * 100
  }

  dollarChange(num1, num2) {
    var x = num1 - num2;
    if (x < 0) {
      return x;
    }
    return "+" + String(x.toFixed(2));
  }

  marketCap(num1) {
    return (num1 * 18658650) / T;
  }

  cleanData(obj) {
    console.log("in here", obj)
    let avgVol = 0;
    let avgPrice = 0;
    let priceOpen = 0;
    let priceClose = 0;
    let priceLow = 0;
    let priceHigh = 0;
    let price = obj['Data']['Data'][INTERVAL]['close'];
    let yesterday = obj['Data']['Data'][INTERVAL - 1]['close'];
    let change = this.percentChange(price, yesterday);
    let dchange = this.dollarChange(price, yesterday);
    let mcap = this.marketCap(price);

    for (let j = 0; j <= this.interval; j++) {
      let tempVol = obj['Data']['Data'][j]['volumeto']
      avgVol = avgVol + tempVol
    }

    avgVol = Math.floor(avgVol / INTERVAL);
    

    for (let j = INTERVAL; j > INTERVAL - 7; j--) {
      let tempPrice = obj['Data']['Data'][j]['close'];
      avgPrice = avgPrice + tempPrice
    }

    avgPrice = Math.floor(avgPrice / 7);

    let priceInner = `<h2>$${price} </h2>`;
    let dchangeInner = `<h3><span class ="change">${dchange}</span></h3>`;
    let changeInner = `<h3><span class ="change">(${change.toFixed(2)}%)</span></h3>`;
    let mcapInner = `<h3>${mcap} </h3>`;
    let avgVolInner = `<h3>${avgVol} </h3>`;
    let avgPriceInner = `<h3>$${avgPrice}</h3>`;


    this.addHtml(".price", priceInner)
    this.addHtml(".change", dchangeInner)
    this.addHtml(".perChange", changeInner)
    this.addHtml(".marketCap", mcapInner)
    this.addHtml(".avgVol", avgVolInner)
    this.addHtml(".avgPrice", avgPriceInner)

    for (var i = 0; i <= this.interval; i++) {
      priceList.push(obj['Data']['Data'][i]['close']);
      var date = new Date(obj['Data']['Data'][i]['time'] * 1000);
      date = date.getUTCMonth() + 1 + "/" + date.getUTCDate();
      this.dates.push(date);
    }

    for (var i = 0; i <= this.interval; i++) {
      priceOpen = (obj['Data']['Data'][i]['open']);
      priceClose = (obj['Data']['Data'][i]['close']);
      priceLow = (obj['Data']['Data'][i]['low']);
      priceHigh = (obj['Data']['Data'][i]['high']);
      date = (obj['Data']['Data'][i]['time'] * 1000)
      let payload = {
        c: priceClose,
        h: priceHigh,
        l: priceLow,
        o: priceOpen,
        t: date
      }
      this.cryDataDay.push(payload)
    }
    this.buildChart();
  }

  buildChart() {
    new Chart(this.ctx, {
      type: 'candlestick',
      data: {
        datasets: [{
          label: 'Bitcoin',
          data: this.cryDataDay,
        }]
      }
    });
  }

  addHtml(className, html) {
    document.querySelector(className).innerHTML = html;
  }
}


cb = new ChartBuilder(INTERVAL)
cb.fetchData(url).then(res => {
  cb.cleanData(res)
})
