$(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('#dtBasicExamplePast').DataTable();
    $('.dataTables_length').addClass('bs-select');
    $('.request').click((e)=>{
        let id = $(e.target).data('id');
        if (id == undefined)
            id = $(e.target).parent().data('id')
        strHref = location.href.replace('history/', '');
        location.href = strHref + '/requests/' + id;
    });
    $('.requestPast').click((e)=>{
        let id = $(e.target).data('id');
        let pet_id = $(e.target).data('pet_id');
        if (id == undefined)
            id = $(e.target).parent().data('id')
        if (pet_id == undefined)
            pet_id = $(e.target).parent().data('pet_id')
        strHref = "http://127.0.0.1:5000/"
        location.href = strHref + 'pets/' + pet_id + '/requests/' + id;
    });
});