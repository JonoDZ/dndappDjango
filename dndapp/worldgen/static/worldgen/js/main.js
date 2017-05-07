/// other stuff
function modalOwnerSet(modalId, ownerId)
{
  var columns = 4;
  var owner = ownerId.innerHTML;
  var modalOwner = $(modalId).find('#modal-owner')[0];
  //remove all previous nodes (clears any previous data assigned)
  while (modalOwner.hasChildNodes()) {
    modalOwner.removeChild(modalOwner.lastChild);
  };
  //text.innerText = ownerId.children.firstName.innerText;
  var table = document.createElement("table");
  //define table head sections
  var tableHead = document.createElement("thead");
  var tableHeadRow = document.createElement("tr");

  //define table body sections
  var tableBody = document.createElement("tbody");
  var tableBodyRow = document.createElement("tr");
  
  //create table entries
  for (i = 0; i < ownerId.childElementCount; i++) {
    var tableBodyRowHeader = document.createElement("th");
    var tableHeadRowHeader = document.createElement("th");
    tableHeadRowHeader.appendChild(document.createTextNode(ownerId.children[i].getAttribute('name')));
    tableBodyRowHeader.appendChild(document.createTextNode(ownerId.children[i].innerText));
    tableHeadRow.appendChild(tableHeadRowHeader);
    tableBodyRow.appendChild(tableBodyRowHeader);
  };
  //construct table head
  tableHeadRow.appendChild(tableHeadRowHeader);
  tableHead.appendChild(tableHeadRow);
  //construct table Body
  tableBodyRow.appendChild(tableBodyRowHeader);
  tableBody.appendChild(tableBodyRow);
  //add all to table and set to modal
  table.appendChild(tableHead);
  table.appendChild(tableBody);
  modalOwner.appendChild(table);
  table.setAttribute('class', "table table-striped table-condensed");
};


function generateDrugModal(itemArray) {
  var modalHeader = document.getElementById('genericModalTheadTr');
  var modalBody = document.getElementById('genericModalTbodyTr');

  modalHeader.innerHTML = '';
  modalBody.innerHTML = '';

  for (thing in itemArray) {modalHeader.innerHTML += "<td>" + thing +"</td>"};

  for (thing in itemArray) {
    modalBody.innerHTML += "<td>" + itemArray[thing] +"</td>";
  };
};

function searchBox() {
    // Declare variables
    var input, filter, tbody, li, a, i;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    tbody = document.getElementById("myTbody");
    tr = tbody.getElementsByTagName('tr');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        if (tr[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        };
    };
};

function constructDieInner(dieDiv, d) {
  var dieDivText = document.createTextNode(genDieNum(d));
  var dieHeader = document.createElement("h5");
  var dieHeaderText = document.createTextNode("D"+d);

  dieHeader.appendChild(dieHeaderText);
  dieDiv.appendChild(dieHeader);
  dieDiv.appendChild(dieDivText);
  return dieDiv;
};

//////////////////////
// Dice Constructor //

function makeDice(dieElem,d) {
  var dieDiv = document.createElement("div");
  dieDiv.className = 'die';
  dieDiv.setAttribute("name", d);

  dieDiv = constructDieInner(dieDiv, d);
  dieElem.appendChild(dieDiv);
};

function addDice(d) {
  var diceBox = $('#diceBox')[0];
  if (d == 0) {diceBox.innerHTML = '';}
  else {makeDice(diceBox,d)};
};

function rerollDice() {
  var diceBox = $('#diceBox')[0];
  var nodes = diceBox.childElementCount;

  for (i = 0; i < nodes; i++) {
    var diceDiv = diceBox.childNodes[i];
    var d = parseInt(diceDiv.getAttribute("name"));

    while (diceDiv.hasChildNodes()) {
      diceDiv.removeChild(diceDiv.lastChild);
    };
    constructDieInner(diceDiv, d);
  };
};

function genDieNum(d) {
  var randomNumber = Math.floor(Math.random()* d) + 1;
  return randomNumber;
};


/////////////////
// sidebar reload 
/////////////////

function randomIntFromInterval(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
};

/////////////////
// side menu updater
//////////////////

$(function(){

	var population = 0;
  $("#citySize li a").click(function(){
    var size = $(event.target).text();
    $("#citySizeText").text($(event.target).text());
    
    //create populations etc by city size
    if(size == 'Hamlet') {
    	var hamlet = [40, 250];
    	population = randomIntFromInterval(hamlet[0],hamlet[1]);
    }
    else if (size == 'Village'){
    	var village = [500, 1500];
    	population = randomIntFromInterval(village[0],village[1]);
    }
    else if (size == 'Town'){
    	var town = [2000, 7000];
    	population = randomIntFromInterval(town[0],town[1]);
    }
    else if(size == 'City'){
    	var city = [9000, 25000];
    	population = randomIntFromInterval(city[0],city[1]);
    };
    $("#population").text(population);
    
 });
});
  

