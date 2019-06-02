$(document).ready(function(){ 
    $("#myInput").on("keyup", function() { 
        var value = $(this).val().toLowerCase(); 
        var pets = $('.pet-title');
        var checkEmpty = false;  
        var nameDog = "";
        pets.each(function(index){
            nameDog = pets[index].innerText.toLowerCase();
            if (nameDog.startsWith(value)) {
                checkEmpty = true; 
                $(pets[index]).closest('.container-pet-card').removeClass('display-none');
            } 
            else { 
                $(pets[index]).closest('.container-pet-card').addClass('display-none'); 
            } 
        })
        if (checkEmpty == false && value != ""){
            if ($('#search').find('.search-popup').length > 0){
                $('.search-popup').remove();
                $('#search').append('<div class="col-md-12 search-popup"><p class="gray-text"> \
                Питомца с таким именем не существует<br /> \ </p> </div>');
            }
            else{
                $('#search').append('<div class="col-md-12 search-popup"><p class="gray-text"> \
                Питомца с таким именем не существует<br /> \ </p> </div>');
            }
        }
        else{
            $('.search-popup').remove();
        } 
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