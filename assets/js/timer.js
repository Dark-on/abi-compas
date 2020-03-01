"use strict";
let deadline = new Date("April 17, 2020 00:00:00").getTime();
window.addEventListener('load', function(){
		function customizeTimer(){
		let now = new Date().getTime();
		let diff = deadline - now;

		let days = Math.floor(diff / (1000 * 60 * 60 * 24));
		let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
		let seconds = Math.floor((diff % (1000 * 60)) / 1000);

		if(hours < 10) hours = "0" + hours; 
		if(minutes < 10) minutes = "0" + minutes; 
		if(seconds < 10) seconds = "0" + seconds; 

		let timer = document.getElementById('timer')
		switch(days){
			case 1:
				timer.innerHTML = `${days} day ${hours}:${minutes}:${seconds}`;
				break;
			case 0:
				timer.innerHTML = `${hours}:${minutes}:${seconds}`;
				break;
			default:
				timer.innerHTML = `${days} days ${hours}:${minutes}:${seconds}`;
		}

		if(diff <= 0 ){
			clearInterval();
			timer.innerHTML = "Пора здавати проект"; 
		}

	}
	customizeTimer();
	setInterval(customizeTimer, 1000);
}, false);