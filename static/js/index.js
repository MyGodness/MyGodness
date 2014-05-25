//flag for different instance for processing
var open=false;

function login(){
	console.log("To log in");

}


function createNewUser() {
		event.preventDefault();
		open = !open;

		if (!open) {
			//create new user
			console.log("Successfully create");
		} else {
		  event.preventDefault();
		  $('.to_hide').slideUp(400,function(){
		    $('.to_show').slideDown();
		  });
		}
	// return false;
 } 


 function reinitial(){
 	$('.to_show').slideUp(400,function(){
 		$('.to_hide').slideDown();
 	});
 	open = false;
 	console.log(open);
 }





