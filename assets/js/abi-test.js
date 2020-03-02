"use strict";
window.addEventListener('DOMContentLoaded', function(){
	let elemIndex = 0,
	prevBut = document.getElementById('prev-btn'),
	nextBut = document.getElementById('next-btn'),
	submitBtn = document.getElementById('submit-btn');
	showElem(elemIndex); 

	prevBut.onclick = function() {
		showElem(elemIndex -=1 );
	}
	nextBut.onclick = function() {
		showElem(elemIndex +=1 );	
	}

	function showElem(n){
		let elements = document.querySelectorAll('.abi-test__item');

		if(n < 0) elemIndex = 0;
		if(n > elements.length - 1) elemIndex = elements.length - 1;

		switch(n){
			case 0:
				prevBut.style.display = 'none';
				nextBut.style.gridColumn = '2/3';
				submitBtn.style.display = 'none';
				break;
			case elements.length - 1:
				nextBut.style.display = 'none';
				submitBtn.style.display = 'block';
				break;
			default:
				prevBut.style.display = 'block';
				nextBut.style.display = 'block';
				prevBut.style.gridColumn = '1/2';
				nextBut.style.gridColumn = '2/3';
				submitBtn.style.display = 'none';
		}

		for (let i = 0; i < elements.length; i++ ){
			elements[i].style.display = "none";
		}
		elements[elemIndex].style.display = "block";	
	}
});