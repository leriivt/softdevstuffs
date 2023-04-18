/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN
   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Crispy Elevator :: Verit Li, Johnathan Song
// SoftDev pd7
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-17m
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //AYO is displayed at the top of the console

var i = "hello"; //when type i and hit ENTER, 'hello' returned
var j = 20; //when type j and hit ENTER, 20 returned


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//f(2) returns 32


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
//when addItem("foo"), foo is added to the numbered list rendered from index.html
//disappears upon refresh


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
//after adding "foo" to list, doing removeItem("foo") results in error
//doing removeItem(9) results in error ("foo" in numbered 9 in the list)
//doing removeItem(8) results in removal of "foo" from list
//(foo is 8th item in list assuming 0 indexing)


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};
//red(0) results in all black colored items in list to be colored red
//doing addItem("foo") after this results in a black foo
//doing red(0) again will result in red foo\

//doing red(<insert number 1-6 inclusive>)
//does not turn any of the blue items in the list red


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
//for all black items in the list starting at top,
//see what color the previous item is
//if previous is blue, color self red
//if previous is red, color self blue


//insert your implementations here for...
// FIB
var fib = function(n){
  if (n == 0) {
      return 0
  }
  else if (n == 1) {
      return 1
  }
  else {
      return fib(n - 1) + fib(n - 2)
  }
}

// FAC
var fact = function(n){
  if (n < 2) {
      return 1
  }
  else { 
      return (n * (fact (n - 1)))
  }
}

// GCD
var gcd = function(a, b) {
  if (a % b === 0){
    return b;
  }
  return gcd(b, a%b);
}


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};