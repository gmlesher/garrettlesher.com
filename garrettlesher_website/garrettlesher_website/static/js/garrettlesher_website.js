const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
    burger.addEventListener('click', () => {
        // Toggle Nav
        nav.classList.toggle('nav-active');

        // ************ if window resized, add resized class with no animations and opacity to 1 ******************
        window.addEventListener('resize', () => {
          if (nav.classList.contains('nav-active')){
            nav.classList.add('resized');
            if (nav.classList.contains('resized')) {
              navLinks.forEach((link, index) => {
                if (link.style.animation) {
                    link.style.opacity = "";
                    link.style.animation = "";
                } else {
                    link.style.opacity = "1";
                    link.style.animation = "";
                }
              });
            }
          } else {
            nav.classList.remove('resized');
          }
        }, true);

        // ************ if burger toggle does not contain the class "toggle", remove animations and opacity **********
        if (!(burger.classList.contains('toggle'))) {
          nav.classList.remove('resized');
          navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.opacity = "";
                link.style.animation = "";
            } else {
                link.style.opacity = "";
                link.style.animation = "";
            }
          });
        }

        // ************ normal animation will play ***************
        // Animate Links
        navLinks.forEach((link, index) => {
              if (link.style.animation) {
                link.style.animation = "";
              } else if (!(burger.classList.contains('toggle'))){
                  link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.4}s`;
              } else {
                link.style.opacity = ""
                nav.classList.remove('resized')
              }
        });

        //  Burger Animation
        burger.classList.toggle('toggle');
    });
}

navSlide();

// on resize window, stop animations
var resizeTimer;
var nav = document.querySelector('.nav-links');
var navLinks = document.querySelectorAll('.nav-links li');
window.addEventListener("resize", () => {
  document.body.classList.add("resize-animation-stopper");

  clearTimeout(resizeTimer);
  resizeTimer = setTimeout(() => {
    document.body.classList.remove("resize-animation-stopper");
  }, 400);
});


// makes all text area fields 3 rows tall
$('form').ready(function() {
  $('textarea').attr({'rows': "3"})
});
