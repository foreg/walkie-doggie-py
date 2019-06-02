$(document).ready(function(){ 
    $("#myInput").on("keyup", function() { 
        var value = $(this).val().toLowerCase(); 
        var pets = $('.item'); 
        console.log(0); 
        pets.each(function(index){ 
            if (pets[index].innerHTML.startsWith(value)) { 
                // $(pets[index]).parent().parent().show(); 
                $(pets[index]).parent().parent().removeClass('display-none');
                console.log($(pets[index]).parent().parent()); 
            } 
            else { 
                // $(pets[index]).parent().parent().hide(); ч
                $(pets[index]).parent().parent().addClass('display-none');
                console.log($(pets[index]).parent().parent()); 
            } 
        }) 
    }); 

    $('.popup-with-zoom-anim').click(function(){
        $('#small-dialog2').data('id', $(this).data('id'));
    });

    $('.confirm').click(function(){
        let pet_id = $(this).parent().parent().data('id');
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