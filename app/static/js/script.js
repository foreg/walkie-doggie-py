new WOW().init();

jQuery.extend( jQuery.fn.pickadate.defaults, {
  monthsFull: [ 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря' ],
  monthsShort: [ 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек' ],
  weekdaysFull: [ 'воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота' ],
  weekdaysShort: [ 'вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб' ],
  today: 'сегодня',
  clear: 'удалить',
  close: 'закрыть',
  firstDay: 1,
  format: 'd mmmm yyyy г.',
  formatSubmit: 'yyyy/mm/dd'
});

$('.datepicker').pickadate();


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

