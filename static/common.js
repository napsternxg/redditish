$(document).ready(function(){
   $(".action").bind("click", function(){
	$pid = $(this).parent().attr("id");
	$voteUrl = "/"+$pid+"/vote";
	$action = "up";
	console.log("Sending AJAX request!!!");
	if($(this).hasClass("up")){
		$action = "up";
	}
	else if($(this).hasClass("down")){
		$action = "down";
	}
	else{
		$action = "undefined";
		console.log("Action Undefined!!!");
		return;
	}
	current = this;
	$.post($voteUrl, {"action" : $action}, function(data){
		console.log(current);
		$votes = $(current).siblings("span.count");
		console.log(data);
		console.log($votes.text());
		$votes.text(parseInt($votes.text()) + parseInt(data));
	});
});
});
