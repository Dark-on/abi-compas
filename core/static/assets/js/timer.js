"use strict";
let deadline = new Date("April 17, 2020 00:00:00").getTime(); //set deadline
window.addEventListener('load', function(){ //browser loaded HTML and external resources
	function customizeTimer(){
		/* find out the current date and the difference between it and the deadline */
		let now = new Date().getTime();
		let diff = deadline - now;

		/* define days, hours, minutes and seconds in the right form */
		let days = Math.floor(diff / (1000 * 60 * 60 * 24));
		let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
		let seconds = Math.floor((diff % (1000 * 60)) / 1000);

		/* formatting */
		if(hours < 10) hours = "0" + hours; 
		if(minutes < 10) minutes = "0" + minutes; 
		if(seconds < 10) seconds = "0" + seconds; 

		let timer = document.getElementById('timer')
		/* fill in html data*/
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

		/* if deadline has come*/
		if(diff <= 0 ){
			clearInterval();
			timer.innerHTML = "Пора здавати проект"; 
		}

	}
	customizeTimer(); //function is called immediately
	setInterval(customizeTimer, 1000); //function is called every second
});