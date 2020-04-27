window.addEventListener('DOMContentLoaded', function () {
    let slides = document.querySelectorAll('.intro__item'),
        arrowNext = document.querySelector('.arrow-next'),
        arrowPrev = document.querySelector('.arrow-prev');

    let slideIndex = 0;
    arrowNext.onclick = () => showSlide(slideIndex +=1);
    arrowPrev.onclick = () => showSlide(slideIndex -=1);
    showSlide(slideIndex);
    function showSlide(index) {
        if (index > 3) slideIndex = 0;
        if (index < 0) slideIndex = 3;

        index = slideIndex;

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
        }

        slides[index].style.display = 'flex';
    }

});