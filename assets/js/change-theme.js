/**
 * An event that starts the timer on the main page after it is loaded.
 * @author Yukhymchuk Yaroslaw
 */
window.addEventListener('load', function(){ //browser loaded HTML and external resources
	/**
     * Need to get button.
     * @type {HTMLElement}
     */
	let butt1 = document.getElementById('button-light'),

	/**
     * Need to get button.
     * @type {HTMLElement}
     */
	butt2 = document.getElementById('button-dark'),

	/**
     * Need to get head.
     * @type {HTMLElement}
     */
	head = document.querySelector('head');

	/* add darktheme link */
	butt2.onclick = function(){
		/*Set style.*/
		butt2.classList.add("active");
		butt1.classList.remove("active");
		/*Customize and set up link to .css file (dark). */
		let link = document.createElement('link');
		link.rel  = 'stylesheet';
		link.type = 'text/css';
		link.id = 'css-dark';
		link.href = '../assets/css/dark-theme.css';
		head.append(link);
	}

	/* delete darktheme link */
	butt1.onclick = function(){
		butt1.classList.add("active");
		butt2.classList.remove("active");
		document.getElementById('css-dark').remove();
	}
});
