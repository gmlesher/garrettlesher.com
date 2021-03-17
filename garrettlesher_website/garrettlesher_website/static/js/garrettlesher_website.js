const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
    burger.addEventListener('click', () => {
        // Toggle Nav
        nav.classList.toggle('nav-active');

        // Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = "";

            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.4}s`;
                console.log(index / 7);
            }
        });
        //  Burger Animation
        burger.classList.toggle('toggle');

    });
}

navSlide();

// on resize window, stop animations
let resizeTimer;
window.addEventListener("resize", () => {
  document.body.classList.add("resize-animation-stopper");
  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    document.body.classList.remove("resize-animation-stopper");
  }, 400);
});

// validation for contact form before submission. Loading animation for 
// contact form here too
$(document).ready(function(){
    $('.needs-validation').on('submit', function(e) {
      if (!this.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
      }
      $(this).addClass('was-validated');
    });

});

// makes all text area fields 3 rows tall
$('form').ready(function() {
  $('textarea').attr({'rows': "3"})
});
