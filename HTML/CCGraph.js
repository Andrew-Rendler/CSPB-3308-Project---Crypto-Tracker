var ctx = document.getElementById('myChart');
var API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f";
var URL_FRAGMENT = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=5";
var url = URL_FRAGMENT + "&api_key=" + API_KEY;
var T = 1000000000000;
var date = 0
var dateDT = luxon.DateTime
var avgVol = 0;
var avgPrice = 0;
var priceOpen = 0;
var priceClose = 0;
var priceLow= 0;
var priceHigh = 0;
var cryDataDay = [];
var cryDataList = [];

fetch(url)
  .then(
    function(response){
      return response.json();
    }
  ).then(function(obj){
    function percentChange(num1,num2){
      return (num1-num2)/num2*100
    }
    function dollarChange(num1,num2){
      var x = num1-num2;
      if (x < 0){
        return x;
      }
      return "+"+String(x.toFixed(2));
    }
    function marketCap(num1){
      return (num1*18658650)/T;
    }
    var price = obj['Data']['Data'][5]['close'];
    var yesterday = obj['Data']['Data'][4]['close'];
    var change = percentChange(price,yesterday);
    var dchange = dollarChange(price,yesterday);
    var volume = obj['Data']['Data'][5]['volumeto'];
    var mcap = marketCap(price);

    for (var j = 0; j <= 5; j++){  
      var tempVol = obj['Data']['Data'][j]['volumeto']
      var tempPrice = obj['Data']['Data'][j]['close'];
      avgVol = avgVol + tempVol
      avgPrice = avgPrice + tempPrice
    }
    avgVol = Math.floor(avgVol / 6);
    avgPrice = Math.floor(avgPrice / 6);

    console.log(obj['Data']['Data']);
    document.querySelector(".price").innerHTML =
      `<h2>$${price} </h2>`;
    document.querySelector(".change").innerHTML =
      `<h3><span class ="change">${dchange}</span></h3>`;
    document.querySelector(".perChange").innerHTML =
      `<h3><span class ="change">(${change.toFixed(2)}%)</span></h3>`;
    document.querySelector(".marketCap").innerHTML =
      `<h3>${mcap} </h3>`;
    document.querySelector(".avgVol").innerHTML =
      `<h3>${avgVol} </h3>`;
    document.querySelector(".avgPrice").innerHTML =
      `<h3>$${avgPrice} </h3>`;

      for (var i = 0; i <= 5; i++){
        priceOpen = (obj['Data']['Data'][i]['open']);
        priceClose = (obj['Data']['Data'][i]['close']);
        priceLow = (obj['Data']['Data'][i]['low']);
        priceHigh = (obj['Data']['Data'][i]['high']);
        date = (obj['Data']['Data'][i]['time']*1000)
        dateDT = date.fromMillis()
        cryDataDay.push(dateDT, priceOpen, priceHigh, priceLow, priceClose);
        cryDataList[i] = cryDataDay;
        cryDataDay = []
      }
    
var barCount = 6;
var initialDateStr = '01 Apr 2017 00:00 Z';

var ctx = document.getElementById('chart').getContext('2d');
ctx.canvas.width = 1000;
ctx.canvas.height = 250; 
var chart = new Chart(ctx, {
	type: 'candlestick',
	data: {
		datasets: [{
			label: 'Bitcoin',
			data: cryDataList,
      /* getRandomData(initialDateStr, barCount) */
		}]
	}
});

var getRandomInt = function(max) {
	return Math.floor(Math.random() * Math.floor(max));
};

function randomNumber(min, max) {
	return Math.random() * (max - min) + min;
}

function randomBar(date, lastClose) {
	var open = randomNumber(lastClose * 0.95, lastClose * 1.05).toFixed(2);
	var close = randomNumber(open * 0.95, open * 1.05).toFixed(2);
	var high = randomNumber(Math.max(open, close), Math.max(open, close) * 1.1).toFixed(2);
	var low = randomNumber(Math.min(open, close) * 0.9, Math.min(open, close)).toFixed(2);
	return {
		t: date.valueOf(),
		o: open,
		h: high,
		l: low,
		c: close
	};

}

function getRandomData(dateStr, count) {
	var date = luxon.DateTime.fromRFC2822(dateStr);
	var data = [randomBar(date, 30)];
	while (data.length < count) {
		date = date.plus({days: 1});
		if (date.weekday <= 5) {
			data.push(randomBar(date, data[data.length - 1].c));
		}
	}
	return data;
}

})

