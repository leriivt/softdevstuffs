// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //Since the useCapture param is set to true for all the event listeners, only the highest one on the DOM tree (table) will show?
  // e.stopPropagation();
  //Prediction was right
};


//Q: Does the order in which the event listeners are attached matter?
// No, even if you move around the event listeners it will still be the same sequence of pop ups

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)
// - No changes seen for table data cell, since there is no event lower than it on the DOM tree
// - For table row, if useCapture is false then cell would display before row. This is because cell is lower than row on the DOM tree.
// - For table, if false then it would go down the DOM tree until it either:
//   a) encounters an event with useCapture set to true or,
//   b) reaches the event at the bottom of the DOM tree

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  // tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  // trs[x].addEventListener('click', clicky, false);
}

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);
