new WOW().init();
$(document).ready(function () {
  $('.nav-button').on('click', function () {
    $('.animated-icon').toggleClass('open');
  })
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        if (this.getAttribute('href') != "#") {
          document.querySelector(this.getAttribute('href')).scrollIntoView({
              behavior: 'smooth'
          });
        }
    });
});

//Accordion
$('.card-link').click(function() {

    if ($(this).parent().parent().hasClass('active')){
      $(this).parent().parent().removeClass('active');
    }
    else{
      $(this).parent().parent().toggleClass('active');
    }
    $currentElem = $(this).parent().parent().html();
    $(".hello").each(function(){
      if ($(this).hasClass('active') && ($(this).html() != $currentElem)){
        $(this).removeClass('active');
      }
    });

    
    // $('#accordion .card').removeClass('active');
    // $(this).closest('.card').addClass('active');

    // var checkElement = $(this).children().next();
    // if (checkElement.is(':visible')){
    //   $(this).removeClass('active');
    // }
    // else{
    //   $(this).addClass('active');
    // }
    

  });
// /Accordion

$('.animated-icon').on('click', function(){
    if (!$('.navbar').hasClass('top-nav-collapse')){
      $('.navbar').toggleClass('top-nav-collapse');
    }
});