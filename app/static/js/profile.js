$(document).ready(function(){ 
    $.getScript("../static/js/magnific-popup.min.js", () => {
        $('.ajax-popup-link').magnificPopup({
            type: 'inline',
            
            fixedContentPos: false,
            fixedBgPos: false,
            
            overflowY: 'auto',
            
            // closeBtnInside: true,
            preloader: false,
            
            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });
        $('.ajax-popup-link-employee').magnificPopup({
            type: 'inline',
            
            fixedContentPos: false,
            fixedBgPos: false,
            
            overflowY: 'auto',
            
            // closeBtnInside: true,
            preloader: false,
            
            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });
    });

    $('.ajax-popup-link').click(function(){
        $('#small-dialog').data('id', $(this).data('id'));
    });
    
    $('.ajax-popup-link-employee').click(function(){
        $('#small-dialog-employee').data('id', $(this).data('id'));
    });

    $('.confirm').click(function(){
        location.reload();
        $.magnificPopup.close()
    });

    $('.dismiss').click(function(){
        $.magnificPopup.close()
    });

});