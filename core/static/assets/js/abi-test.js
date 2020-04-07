"use strict";
window.addEventListener('DOMContentLoaded', function(){ //loaded html but no styles and so on
	let elemIndex = 0,
	/* get the buttons from html */
	prevBut = document.getElementById('prev-btn'),
	nextBut = document.getElementById('next-btn'),
	submitBtn = document.getElementById('submit-btn');
	showElem(elemIndex); // show first elem

	/* calls the function and increases the element index by 1 */
	prevBut.onclick = function() {
		showElem(elemIndex -=1 );
	}
	/* calls the function and decreases the element index by 1 */
	nextBut.onclick = function() {
		showElem(elemIndex +=1 );	
	}

	/* function that shows an element */
	function showElem(n){
		let elements = document.querySelectorAll('.abi-test__item');

		if(n < 0) elemIndex = 0;
		if(n > elements.length - 1) elemIndex = elements.length - 1;

		/* style-changing conditions */
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

		/* display:none all elements */
		for (let i = 0; i < elements.length; i++ ){
			elements[i].style.display = "none";
		}
		/* show elem with curent index */
		elements[elemIndex].style.display = "block";	
	}
});