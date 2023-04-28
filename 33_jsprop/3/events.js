// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // We think that it will stop the additional pop-ups from appearing, so only the cell inner HTML will appear
  // We were right in that it stopped after only one, but it was the entire table inner html not the cell. This is because of event capturing is set to true in line 31.
  e.stopPropagation();
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)

// The boolean arg represents useCapture, which determines the order in which events are sent to the listener. If set to true, events highest in the DOM tree will be sent to the listener first. Otherwise, if false it will be events lower in the tree.

// table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, false);

// Q: When user clicks on a cell, in what order will the pop-ups appear?
