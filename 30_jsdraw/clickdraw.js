//retrieve node in DOM via ID
var c = Document.getContext("slate")

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//var toggleMode = function(e) {
var toggleMode = (e) => {
    console.log("toggling...");
    if () {


    }
    else {

    }
}

var drawRect = function(e) {
    var event = MouseEvent();
    var mouseX = e.clientX;
    var mouseY = e.clientY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    fillRect(mouseX, mouseY, 100, 200);
}

//var drawCircle = function(e) {
var drawCircle = (e) => {
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function() {
var draw = (e) => {

}

//var wipeCanvas = function() {
var wipeCanvas = () => {

}

c.addEventListener("click", draw);

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);

var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);

