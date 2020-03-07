"use strict";
window.addEventListener('load', function(){ //browser loaded HTML and external resources
	/* get the buttons from html */
	let butt1 = document.getElementById('button-light'),
	butt2 = document.getElementById('button-dark'),
	head = document.querySelector('head');

	/* add darktheme link */
	butt2.onclick = function(){
		butt2.classList.add("active");
		butt1.classList.remove("active");
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
