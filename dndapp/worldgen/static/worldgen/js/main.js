 /// other stuff
 function modalOwnerSet(modalId, ownerId)
 {
    var text = $(modalId).find('#modal-owner')[0];
    //text.innerText = ownerId.children.firstName.innerText;
    text.innerHTML = "<tr>" + ownerId.innerHTML + "</tr>"
 }

function searchBox() {
    // Declare variables
    var input, filter, ul, li, a, i;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}
 /////////////////
  // sidebar reload 
  //////////////////

	function randomIntFromInterval(min,max)
	{
	    return Math.floor(Math.random()*(max-min+1)+min);
	}

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
      	population = randomIntFromInterval(hamlet[0],hamlet[1])
      }
      else if (size == 'Village'){
      	var village = [500, 1500];
      	population = randomIntFromInterval(village[0],village[1])
      }
      else if (size == 'Town'){
      	var town = [2000, 7000];
      	population = randomIntFromInterval(town[0],town[1])
      }
      else if(size == 'City'){
      	var city = [9000, 25000];
      	population = randomIntFromInterval(city[0],city[1])
      }
      $("#population").text(population);
      
   });
});
  

