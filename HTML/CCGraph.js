var API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f";
var URL_FRAGMENT = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=5";
var url = URL_FRAGMENT + "&api_key=" + API_KEY;
var T = 1000000000000;
var date = 0
var avgVol = 0;
var avgPrice = 0;
var priceOpen = 0;
var priceClose = 0;
var priceLow= 0;
var priceHigh = 0;
var cryDataDay = [];


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
        payload = {
          c: priceClose,
          h: priceHigh,
          l: priceLow,
          o: priceOpen,
          t: date
        }
        cryDataDay.push(payload)
      }

var ctx = document.getElementById('chart').getContext('2d');
ctx.canvas.width = 1000;
ctx.canvas.height = 250; 
var chart = new Chart(ctx, {
	type: 'candlestick',
	data: {
		datasets: [{
			label: 'Bitcoin',
			data: cryDataDay,
		}]
	}
});


})
