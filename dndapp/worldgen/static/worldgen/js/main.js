  /////////////////
  // sidebar reload 
  //////////////////

	function randomIntFromInterval(min,max)
	{
	    return Math.floor(Math.random()*(max-min+1)+min);
	}
/*
  $(function() {

  	//ON REROLL
    $('#rerollAll').bind('click', function() {
      var npcQuant = $('input[name="npcGenQuant"]').val();
      window.location.href = "//192.168.1.11:8000/world/"+npcQuant+"/regennpcs/";

    });
  });
*/
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
  

