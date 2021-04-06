gsap.registerPlugin(ScrollTrigger);

// validation for contact form before submission. Loading animation for 
// contact form here too
$(document).ready(function(){
    // dark theme for recaptcha
    $('.g-recaptcha').attr('data-theme', 'dark');
    // validate forms before submission
    $('.needs-validation').on('submit', function(e) {
        if (!this.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
        } 
        $(this).addClass('was-validated');
    });
});

// tilt animations based on window width. animation disabled on small screens (mobile)
function handleAnimations() {
    var width = $(window).width();
    if (width >= 768) {
        // if ".js-tilt" class doesn't exist...
        if ($('.js-tilt').length == 0) {
            // add ".js-tilt" class and build animation
            $('.project').addClass('js-tilt');
            // ****** note that ".js-tilt" class automatically adds *********
            // ****** ".js-tilt-glare" & ".js-tilt-glare-inner" classes *****
            $('.js-tilt').tilt({
                maxTilt: 12,
                perspective: 1500,
                glare: true,
                maxGlare: .02,
                gyroscope: true,
            });
        }
    // if screen is wider than 768, remove all classes and styles
    // associated with animations
    } else {
        $('.project').removeClass('js-tilt');
        $('.project > div > div.js-tilt-glare-inner').remove();
        $('.project > div.js-tilt-glare').remove();
        $('.project').removeAttr('style');
    } 
}

// calls tilt animations when document ready and on window resizes. 
// resize has own rule
$(document).ready(function(){
   $(window).resize(function() {
      handleAnimations();
      $('.project').css('transform', 'none !important');
   });
   handleAnimations();
});

// apply mask to project image on hover, remove when leaving hover
function addMask() {
    $('.project > a').hover(function(){
        // get current card id
        var currentCard = this.id;
        // get current mask
        var currentMask = $(`#${currentCard} > div.projectImage > div`);
        // set opacity on mask during hover
        $(currentMask).css('opacity', '0.9');
    }, function(){
        // get current card id
        var currentCard = this.id;
        // get current mask
        var currentMask = $(`#${currentCard} > div.projectImage > div`);
        // set opacity on mask after hover
        $(currentMask).css('opacity', '');
    });
}
addMask();


// arrow animation
gsap.to(".arrow", {
    scrollTrigger: {
        trigger: ".aboutRow",
        start: "top bottom",
        end: "+=250",
        scrub: .5,
    },
    y: "+=250",
    xPercent: -100,
    rotation: -45,
    ease: "none",
    duration: 2,
});
