/**
* An event that is caused when DOM content loaded on page.
* @author Yukhymchuk Yaroslaw
* 
*/
window.addEventListener('DOMContentLoaded', function () {
    /**
     * Need to get slides.
     * @type {HTMLCollection}
     */
    let slides = document.querySelectorAll('.intro__item'),
    /**
     * Need to get arrowNext.
     * @type {HTMLElement}
     */
        arrowNext = document.querySelector('.arrow-next'),
    /**
     * Need to get arrowPrev.
     * @type {HTMLElement}
     */
        arrowPrev = document.querySelector('.arrow-prev'),
    /**
     * Need to get dots.
     * @type {HTMLCollection}
     */
        dots = document.querySelectorAll('.dot');

    /**
     * Need to exlain slide index.
     * @type {number}
     */
    let slideIndex = 0;


    /*Add eventListeners on dots*/
    for (let i = 0; i < dots.length; i++) {
        dots[i].onclick = function () {
            slideIndex = i;
            showSlide(slideIndex);
        }
    }

    /**
     * Event listeners for clicks on the buttons.
     */
    arrowNext.onclick = () => showSlide(slideIndex += 1);
    arrowPrev.onclick = () => showSlide(slideIndex -= 1);

    /*Need to initial display first slide.*/
    showSlide(slideIndex);

    /**
     * Shows slide with the desired index.
     * @param {number} index - The index of the slide.
     */
    function showSlide(index) {
        if (index > 3) slideIndex = 0;
        if (index < 0) slideIndex = 3;

        index = slideIndex;
        
        /*Clear style.*/
        slides.forEach(slide => slide.style.display = "none");
        dots.forEach(dot => dot.classList.remove("active"));

        /*Set style.*/
        dots[index].classList.add("active");
        slides[index].style.display = 'flex';
        return slideIndex;
    }

});