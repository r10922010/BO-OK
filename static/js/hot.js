
$(document).ready(function() {
	$("header").mouseover(function() {
		$(this).addClass("color_header");
	});

	$("header").mouseleave(function() {
		$(this).removeClass("color_header");
	});
})

$(function () {
	$(".jumbotron").css({
		"background-image": "linear-gradient(rgba(255,255,255,0.6), rgba(255,255,255,0.6)), url('/static/images/coffee.jpg')",
		"background-size": "cover",
		"height": "100%",
		"background-position": "center",
		"background-repeat": "no-repeat",
	});
})