/*** 
* An event that is caused when DOM content loaded on page.
* @author Yukhymchuk Yaroslaw
* 
*/
window.addEventListener('DOMContentLoaded', function () {
	/**
	 * Need to explain index of element.
	 * @type {number}
	 */
	let elemIndex = 0,

	/**
	* Need to get buttons.
	* @type {HTMLCollection}
	*/
	btns = document.querySelector('.buttons'),

	/**
	* Need to get prev btn.
	* @type {HTMLElement}
	*/
	prevBut = document.getElementById('prev-btn'),

	/**
	* Need to get next btn.
	* @type {HTMLElement}
	*/
	nextBut = document.getElementById('next-btn'),

	/**
	* Need to get submit button.
	* @type {HTMLElement}
	*/
	submitBtn = document.getElementById('submit-btn');

	/*Show first elem */
	showElem(elemIndex); // 

	/* Calls the function and increases the element index by 1 */
	prevBut.onclick = function () {
		showElem(elemIndex -= 1);
	}
	/* Calls the function and decreases the element index by 1 */
	nextBut.onclick = function () {
		showElem(elemIndex += 1);
	}

	/* function that shows an element */
	function showElem(n) {
		/**
		* Need to get items of test.
		* @type {HTMLCollection}
  		*/
		let elements = document.querySelectorAll('.abi-test__item');

		if (n < 0) elemIndex = 0;
		if (n > elements.length - 1) elemIndex = elements.length - 1;

		/* Style-changing conditions */
		switch (n) {
			case 0:
				prevBut.style.display = 'none';
				submitBtn.style.display = 'none';
				btns.style.justifyContent = 'flex-end';
				break;
			case elements.length - 1:
				nextBut.style.display = 'none';
				submitBtn.style.display = 'block';
				btns.style.justifyContent = 'space-between';
				break;
			default:
				prevBut.style.display = 'block';
				nextBut.style.display = 'block';
				submitBtn.style.display = 'none';
				btns.style.justifyContent = 'space-between';
		}

		/* Display:none all elements */
		elements.forEach(element => element.style.display = "none");

		/* Show elem with curent index */
		elements[elemIndex].style.display = "block";
	}
});