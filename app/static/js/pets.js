$(document).ready(function(){ 
    $("#myInput").on("keyup", function() { 
        var value = $(this).val().toLowerCase(); 
        var items = $('.item'); 
        console.log(0); 
        items.each(function(index){ 
            if (items[index].innerHTML.startsWith(value)) { 
                // $(items[index]).parent().parent().show(); 
                $(items[index]).parent().parent().removeClass('display-none');
                console.log($(items[index]).parent().parent()); 
            } 
            else { 
                // $(items[index]).parent().parent().hide(); ч
                $(items[index]).parent().parent().addClass('display-none');
                console.log($(items[index]).parent().parent()); 
            } 
        }) 
    }); 

    $('.popup-with-zoom-anim').click(function(){
        $('#small-dialog').data('id', $(this).data('id'));
    });

    $('.confirm').click(function(){
        let pet_id = $(this).parent().data('id');
        $.ajax({
            url: '/pets/' + pet_id,
            type: 'DELETE',
            success: function(result) {
                location.reload();
            }
        });
        $.magnificPopup.close()
    });

    $('.dismiss').click(function(){
        $.magnificPopup.close()
    });

    $.getScript("static/js/magnific-popup.min.js", () => {
        $('.popup-with-zoom-anim').magnificPopup({
            type: 'inline',
            
            fixedContentPos: false,
            fixedBgPos: true,
            
            overflowY: 'auto',
            
            closeBtnInside: true,
            preloader: false,
            
            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });
    });
});