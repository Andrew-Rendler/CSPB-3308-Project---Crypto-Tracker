var bitlist = []
var dogelist = []
var etherlist = []
var bitval = {};
var dogeval = {};
var etherval = {};
var storeval = {
  ".price": "doge",
  ".change": "doge",
  ".perChange": "doge",
  ".marketCap": "doge",
  ".avgVol": "doge",
  ".avgPrice": "doge",
  ".news": "DOGE NEWS"
};

function displayBit() {
  var crypt = document.querySelector(".bit")
  if (crypt.id == "bitid"){
    return
  }
  else if(crypt.id == "dogeid"){
    for (var i in storeval){
      dogeval[i] = document.querySelector(i).innerHTML
    }
    if (!dogelist.length){
      dogelist = cb.popChart().reverse()
    }
    else{
      cb.deleteChart()
      }
    }
  else if(crypt.id == "etherid"){
    for (var i in storeval){
      etherval[i] = document.querySelector(i).innerHTML
    }
    if (!etherlist.length){
      etherlist = cb.popChart().reverse();
    }
    else{
      cb.deleteChart();
    }
  }
  cb.fillHTML(bitval)
  cb.chart.data.datasets[0].label = 'Bitcoin'
  crypt.id = "bitid"
  cb.fillChart(bitlist)
}

function displayDoge() {
  var crypt = document.querySelector(".bit")
  if (crypt.id == "dogeid"){
    return
  }
  else if (crypt.id == "bitid"){
    for (var i in storeval){
      bitval[i] = document.querySelector(i).innerHTML
    }
    if (!bitlist.length){
      bitlist = cb.popChart().reverse()
    }
    else{
      cb.deleteChart()
    }
  }
  else if (crypt.id == "etherid"){
    for (var i in storeval){
      etherval[i] = document.querySelector(i).innerHTML
    }
    if (!etherlist.length){
      etherlist = cb.popChart().reverse();
    }
    else{
      cb.deleteChart();
    }
  }
  crypt.id = "dogeid"
  cb.chart.data.datasets[0].label = 'Dogecoin'
  if (!dogelist.length){
    fetch(urlDoge)
      .then(res => res.json())
      .then(data => cb.cleanData(data))
      .then(any => cb.updateChart());
  }
  else{
    cb.fillHTML(dogeval)
    cb.fillChart(dogelist)
  }
}

function displayEther(){
  var crypt = document.querySelector(".bit")
  if (crypt.id == "etherid"){
    return
  }
  else if (crypt.id == "bitid"){
    for (var i in storeval){
      bitval[i] = document.querySelector(i).innerHTML
    }
    if (!bitlist.length){
      bitlist = cb.popChart().reverse()
    }
    else{
      cb.deleteChart()
    }
  }
  else if (crypt.id == "dogeid"){
    for (var i in storeval){
      dogeval[i] = document.querySelector(i).innerHTML
    }
    if (!dogelist.length){
      dogelist = cb.popChart().reverse();
    }
    else{
      cb.deleteChart();
    }
  }
  crypt.id = "etherid"
  cb.chart.data.datasets[0].label = 'Ethereum'
  if (!etherlist.length){
    fetch(urlEther)
      .then(res => res.json())
      .then(data => cb.cleanData(data))
      .then(any => cb.updateChart());
  }
  else{
    cb.fillHTML(etherval)
    cb.fillChart(etherlist)
  }
}
