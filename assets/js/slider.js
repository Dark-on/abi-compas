window.addEventListener('DOMContentLoaded', function () {
    let slides = document.querySelectorAll('.intro__item'),
        arrowNext = document.querySelector('.arrow-next'),
        arrowPrev = document.querySelector('.arrow-prev'),
        dots = document.querySelectorAll('.dot');

    let slideIndex = 0;
    for (let i = 0; i < dots.length; i++){
        dots[i].onclick = function(){
            slideIndex = i;
            showSlide(slideIndex);
        }
    }

    arrowNext.onclick = () => showSlide(slideIndex +=1);
    arrowPrev.onclick = () => showSlide(slideIndex -=1);
    showSlide(slideIndex);
    function showSlide(index) {
        if (index > 3) slideIndex = 0;
        if (index < 0) slideIndex = 3;

        index = slideIndex;

        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
            dots[i].classList.remove("active");
        }
        dots[index].classList.add("active");
        slides[index].style.display = 'flex';
    }

});