$('#submit').click(function() {
    if($('#star1').is(':checked')) { $('#Rating').val("1"); }
    if($('#star2').is(':checked')) { $('#Rating').val("2"); }
    if($('#star3').is(':checked')) { $('#Rating').val("3");}
    if($('#star4').is(':checked')) { $('#Rating').val("4"); }
    if($('#star5').is(':checked')) { $('#Rating').val("5"); }
 });