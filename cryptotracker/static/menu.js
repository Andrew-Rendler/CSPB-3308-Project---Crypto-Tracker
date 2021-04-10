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
};

function displayBit() {
  var crypt = document.querySelector(".bit")
  var theme = document.querySelector(".theme").innerHTML;
  var y = document.querySelectorAll(".active")
  for (var i = 0; i < 3; i++){
    if (y[i].id == "bitbtn"){
      y[i].style.color = "#ff6666";
    }
    else if(theme == "Dark Theme"){
      y[i].style.color = "black";
    }
    else{
      y[i].style.color = "white";
    }

  }
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
  var theme = document.querySelector(".theme").innerHTML;
  var y = document.querySelectorAll(".active")
  for (var i = 0; i < 3; i++){
    if (y[i].id == "dogebtn"){
      y[i].style.color = "#ff6666";
    }
    else if(theme == "Dark Theme"){
      y[i].style.color = "black";
    }
    else{
      y[i].style.color = "white";
    }

  }
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
  var theme = document.querySelector(".theme").innerHTML;
  var y = document.querySelectorAll(".active")
  for (var i = 0; i < 3; i++){
    if (y[i].id == "etherbtn"){
      y[i].style.color = "#ff6666";
    }
    else if(theme == "Dark Theme"){
      y[i].style.color = "black";
    }
    else{
      y[i].style.color = "white";
    }

  }
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

function theme(){
  var theme = document.querySelector(".theme").innerHTML;
  if (theme == "Light Theme"){
    document.getElementById("body").style.backgroundColor = "white";
    document.querySelector(".theme").innerHTML = "Dark Theme";
    document.querySelector(".menu").style.backgroundColor = "white";
    document.querySelector(".price").style.color = "black";
    var x = document.querySelectorAll(".data");
    for (var i =0; i < 3; i++){
      x[i].style.color = "black";
    }
    var y = document.querySelectorAll(".active")
    for (var i =0; i < 4; i++){
      y[i].style.color = "black";
    }
    var z = document.querySelectorAll(".headline")
    for (var i =0; i < 5; i++){
      z[i].style.color = "black";
    }
    var a = document.querySelectorAll(".hr")
    for (var i =0; i < 4; i++){
      a[i].style.color = "black";
    }
    document.querySelector(".output").style.color = "black";
    document.querySelector(".output").style.backgroundColor = "white";

  }
  else if (theme == "Dark Theme"){
    document.getElementById("body").style.backgroundColor = "#111122"
    document.querySelector(".theme").innerHTML = "Light Theme"
    document.querySelector(".menu").style.backgroundColor = "#111122"
    document.querySelector(".price").style.color = "#eeeeff";
    var x = document.querySelectorAll(".data");
    for (var i =0; i < 3; i++){
      x[i].style.color = "#eeeeff";
    }
    var y = document.querySelectorAll(".active")
    for (var i =0; i < 4; i++){
      y[i].style.color = "#dddddd";
    }
    var z = document.querySelectorAll(".headline")
    for (var i =0; i < 5; i++){
      z[i].style.color = "white";
    }
    var a = document.querySelectorAll(".hr")
    for (var i =0; i < 4; i++){
      a[i].style.color = "white";
    }
    document.querySelector(".output").style.color = "white";
    document.querySelector(".output").style.backgroundColor = "black";

  }
}
