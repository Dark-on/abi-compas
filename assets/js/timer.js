"use strict";
let deadline = new Date("May 21, 2020 00:00:00").getTime();
window.onload = function(){
	function customizeTimer(){
		let now = new Date().getTime();
		let diff = deadline - now;

		let days = Math.floor(diff / (1000 * 60 * 60 * 24));
		let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
		let seconds = Math.floor((diff % (1000 * 60)) / 1000);

		let timer = document.getElementById('timer')
		timer.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

		if(diff <= 0 ){
			clearInterval();
			timer.innerHTML = "Пізда настала"; 
		}

	}
	customizeTimer();
	setInterval(customizeTimer, 1000);
}
