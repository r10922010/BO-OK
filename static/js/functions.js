$(document).ready(function() {
	var item_count = $('.menu .col-md-4').length;
	console.log("test");
	$('.menu-btn-left').click(function() {
		var carsize = $('.menu .col-md-4').width();
		var currentT = $('.menu-row').css('transform').split(/[()]/)[1];
		var posX = currentT.split(',')[4];
		var left_offset = parseInt(posX) + (parseInt(carsize) + 31)*3;

		if (parseInt(posX)*-1 >= 0) {
			$('.menu-row').css(
				"transform", "translateX("+left_offset+"px)"
			);
		}
	});

	$('.menu-btn-right').click(function() {
		var item_count = parseInt($('.menu .col-md-4').length) - 2;
		var carsize = $('.menu .col-md-4').width();
		var currentT = $('.menu-row').css('transform').split(/[()]/)[1];
		var posX = currentT.split(',')[4];
		var right_offset = parseInt(posX) - (parseInt(carsize) + 31)*3;

		if (parseInt(posX)*-1 <= (parseInt(carsize)+30)*(parseInt(item_count)-1)) {
			$('.menu-row').css(
				"transform", "translateX("+right_offset+"px)"
			);
		}
	});
})