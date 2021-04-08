var API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f";
var INTERVAL = 100
var URL_FRAGMENT = `https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=${INTERVAL}`;
var URL_FRAGMENT_DOGE = `https://min-api.cryptocompare.com/data/v2/histoday?fsym=DOGE&tsym=USD&limit=${INTERVAL}`;
var URL_FRAGMENT_ETHER = `https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=${INTERVAL}`;
var url = URL_FRAGMENT + "&api_key=" + API_KEY;
var urlDoge = URL_FRAGMENT_DOGE + "&api_key=" + API_KEY;
var urlEther = URL_FRAGMENT_ETHER + "&api_key=" + API_KEY;
var T = 1000000000000;
var NUM_DOGE = 129090000000
var NUM_BTC = 18658650
var NUM_ETHER = 115360000

class ChartBuilder {
  constructor(interval) {
    this.cryDataDay = []
    this.interval = interval;
    this.ctx = document.getElementById('chart').getContext('2d')
    this.ctx.canvas.width = 1000;
    this.ctx.canvas.height = 600;
    this.chart = null
  }

  fetchData(url) {
    return fetch(url).then(res => {
      return res.json()
    })
  }

  percentChange(num1, num2) {
    return ((num1 - num2) / num2 * 100).toFixed(2)
  }

  dollarChange(num1, num2) {
    var x = num1 - num2;
    if (x < 0) {
      return x.toFixed(2);
    }
    return "+" + x.toFixed(2);
  }

  marketCap(num1) {
    if (document.querySelector(".bit").id == "bitid")
      return ((num1 * NUM_BTC) / T).toFixed(3);
    if (document.querySelector(".bit").id == "dogeid")
      return ((num1 * NUM_DOGE) / T).toFixed(3);
    if (document.querySelector(".bit").id == "etherid")
      return ((num1 * NUM_ETHER) / T).toFixed(3);
  }

  cleanData(obj) {
    console.log("in here", obj)
    this.cryDataDay = [];
    let avgVol = 0;
    let avgPrice = 0;
    let priceOpen = 0;
    let priceClose = 0;
    let priceLow = 0;
    let priceHigh = 0;
    let date = 0;
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

    let priceInner = `$${price.toFixed(2)}`;
    let dchangeInner = `${dchange}`;
    let changeInner = `${change}%`;
    let mcapInner = `$${mcap}T`;
    let avgVolInner = `${avgVol}`;
    let avgPriceInner = `$${avgPrice}`;

    this.addHtml(".price", priceInner)
    this.addHtml(".change", dchangeInner)
    this.addHtml(".perChange", changeInner)
    this.addHtml(".marketCap", mcapInner)
    this.addHtml(".avgVol", avgVolInner)
    this.addHtml(".avgPrice", avgPriceInner)
    if (document.querySelector(".bit").id == "bitid"){
      this.addHtml(".news","BITCOIN NEWS")
    }
    else if (document.querySelector(".bit").id == "dogeid"){
      this.addHtml(".news","DOGECOIN NEWS")
    }
    else {
      this.addHtml(".news","ETHEREUM NEWS")
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
  }

  updateChart(){
    for (let i = 0; i <= this.interval; i++){
      this.chart.data.datasets.forEach((dataset) => {
          dataset.data.push(this.cryDataDay[i]);
      });
    }
    this.chart.update();
  }

  fillChart(list){
    for (let i = 0; i <= this.interval; i++){
      this.chart.data.datasets.forEach((dataset) => {
          dataset.data.push(list[i]);
      });
    }
    this.chart.update();
  }

  fillHTML(obj){
    for (var i in obj){
      document.querySelector(i).innerHTML = obj[i]
    }
  }

  popChart(){
    var list = []
    for (let i = 0; i <= this.interval; i++){
      this.chart.data.datasets.forEach((dataset) => {
          list.push(dataset.data.pop());
      });
    }
    return list
  }

  deleteChart(){
    for (let i = 0; i <= this.interval; i++){
      this.chart.data.datasets.forEach((dataset) => {
          dataset.data.pop();
      });
    }

  }

  buildChart() {
    this.chart = new Chart(this.ctx, {
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
  cb.buildChart(res)
})
