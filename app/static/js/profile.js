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
        $('.ajax-popup-link-active').magnificPopup({
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

    $('.ajax-popup-link-active').click(function(){
        $('#small-dialog-active').data('id', $(this).data('id'));
    });

    $('.confirm').click(function(){
        location.reload();
        $.magnificPopup.close()
    });

    $('.dismiss').click(function(){
        $.magnificPopup.close()
    });

    $('.request').click((e)=>{
        let id = $(e.target).data('id');
        if (id == undefined)
            id = $(e.target).parent().data('id')
        location.href += '/requests/' + id;
    });

});