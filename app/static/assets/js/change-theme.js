"use strict";
window.onload = function (){
	let butt1 = document.getElementById('button-light'),
	butt2 = document.getElementById('button-dark'),
	arrImg = document.querySelectorAll("img");
	butt1.onclick = function(){
		butt1.classList.add("active");
		butt2.classList.remove("active");
		document.body.style.filter = null;
		for (let i = 0; i < arrImg.length; i++) arrImg[i].style.filter = null;
	}
	butt2.onclick = function(){
		butt2.classList.add("active");
		butt1.classList.remove("active");
		document.body.style.filter = "invert(.9) hue-rotate(180deg)";
		//for (let i = 0; i < arrImg.length; i++) arrImg[i].style.filter = "invert(1) hue-rotate(180deg)";
	}
}