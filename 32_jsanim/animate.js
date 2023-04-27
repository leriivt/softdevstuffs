// Team PreView :: Prattay Dey, Verit Li
// SoftDev pd07
// K31 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#00ffff";

// init global var for use w animation frames
var requestID;

var clear = (e) => {
    //e.preventDefault();

    console.log("wiping canvas...")
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
    console.log("ET VIOLA.  eh?")
}

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.floor(Math.random() * (c.width - rectWidth));
    var rectY = Math.floor(Math.random() * (c.height - rectHeight));

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        clear(c);
    
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    
        if (rectX <= 0 || rectX >= c.width-rectWidth) {
            xVel *= -1;
        }
        if (rectY <= 0 || rectY >= c.height-rectHeight) {
            yVel *= -1;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo();
}



var radius = 0;
var growing = true;

var drawDot = () => {
    console.log("drawDot invoked...");

    //so no speed up, cancels the current animation
    window.cancelAnimationFrame(requestID);
    
    // wipes canvas
    clear(c);

    //repaints circle
    ctx.beginPath();
    ctx.arc(playground.width/2, playground.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();

    //tell circle to grow or shrink
    if (growing == true) {
        radius += 1;
    }
    else {
        radius -= 1;
    }

    //check if wall hit or singularity reached
    if (radius*2 >= playground.width || radius <= 0) {
        growing = !growing;
    }
    
    //says that theres an animation and call drawDot again for next frame
    requestID = window.requestAnimationFrame(drawDot);

}

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log( requestID );
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);