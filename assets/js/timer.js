/**
 * An event that starts the timer on the main page after it is loaded.
 * @author Yukhymchuk Yaroslaw
 */
window.addEventListener('load', function () { //browser loaded HTML and external resources
	/**
	 * This func need to customize timer.
	 */
	function customizeTimer() {
		/**
		 * Need to set deadline.
		 * @type {number}
		 */
		let deadline = new Date("May 20, 2020 00:00:00").getTime();

		/**
		 * Need to get now time/
		 * @type {number}
		 */
		let now = new Date().getTime();

		/**
		 * Find out the current date and the difference between it and the deadline.
		 * @type {number}
		 */
		let diff = deadline - now;

		/**
		 * Define days.
		 * @type {number}
		 */
		let days = Math.floor(diff / (1000 * 60 * 60 * 24));

		/**
 		* Define hours.
		* @type {number}
 		*/
		let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));

		/**
 		* Define minutes.
 		* @type {number}
 		*/
		let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

		/**
 		* Define seconds.
 		* @type {number}
 		*/
		let seconds = Math.floor((diff % (1000 * 60)) / 1000);

		/*Formatting. */
		if (hours < 10) hours = "0" + hours;
		if (minutes < 10) minutes = "0" + minutes;
		if (seconds < 10) seconds = "0" + seconds;

		/**
		 * Need to get timer from html.
		 * @type {HTMLElement}
		 */
		let timer = document.getElementById('timer')

		/*Formating*/
		switch (days) {
			case 1:
				timer.innerHTML = `${days} day ${hours}:${minutes}:${seconds}`;
				break;
			case 0:
				timer.innerHTML = `${hours}:${minutes}:${seconds}`;
				break;
			default:
				timer.innerHTML = `${days} days ${hours}:${minutes}:${seconds}`;
		}

		if (diff <= 0) {
			clearInterval(tik);
			timer.innerHTML = "Пора здавати проект";
		}

	}

	/*Function is called immediately */
	customizeTimer(); 

	/*function is called every second */
	let tik = setInterval(customizeTimer, 1000);
});