var ctx = document.getElementById('myChart');
var API_KEY = "15bbc2af04315d0d116d7a99909e23d0a026a0ebf729cb0033d82295b3748d6f";
var URL_FRAGMENT = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=5";
var url = URL_FRAGMENT + "&api_key=" + API_KEY;
var T = 1000000000000;
var priceList = [];
var dates = [];

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
    console.log(obj['Data']['Data']);
    document.querySelector(".price").innerHTML =
      `<h1>$${price} <span class ="change">${dchange} (${change.toFixed(2)}%)</span></h1>`;
    document.querySelector(".info").innerHTML =
      `
       <h3>Volume: $${volume.toFixed()} </h3>
       <h3>Market Cap: $${mcap.toFixed(3)}T </h3>`;
    for (var i = 0; i <= 5; i++){
      priceList.push(obj['Data']['Data'][i]['close']);
      var date = new Date(obj['Data']['Data'][i]['time']*1000);
      date = date.getUTCMonth() + 1 + "/" + date.getUTCDate();
      dates.push(date);
    }
    var myChart = new Chart(ctx, {
       type: 'line',
       data: {
           labels: dates,
           datasets: [{
               label: 'BTC Price',
               data: priceList,
               backgroundColor: [
                   'rgba(255, 99, 132, 0.2)',
                   'rgba(54, 162, 235, 0.2)',
                   'rgba(255, 206, 86, 0.2)',
                   'rgba(75, 192, 192, 0.2)',
                   'rgba(153, 102, 255, 0.2)',
                   'rgba(255, 159, 64, 0.2)'
               ],
               borderColor: [
                   'rgba(255, 99, 132, 1)',
                   'rgba(54, 162, 235, 1)',
                   'rgba(255, 206, 86, 1)',
                   'rgba(75, 192, 192, 1)',
                   'rgba(153, 102, 255, 1)',
                   'rgba(255, 159, 64, 1)'
               ],
               borderWidth: 1
           }]
       },
       options: {
           scales: {
               yAxes: [{
                   ticks: {
                       beginAtZero: false
                   }
               }]
           }
       }
  });
})
