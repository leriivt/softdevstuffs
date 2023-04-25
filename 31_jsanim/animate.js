// Team PreView :: Prattay Dey, Verit Li
// SoftDev pd07
// K31 -- canvas based JS animation
// 2023-04-25t

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#00ffff";

// init global var for use w animation frames
var requestID;

var clear = (e) => {
    console.log("wiping canvas...")
    ctx.clearRect(0,0,c.clientWidth,c.clientHeight)
    console.log("ET VIOLA.  eh?")
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
stopButton.addEventListener("click", stopIt);