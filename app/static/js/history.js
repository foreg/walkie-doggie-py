$(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('.dataTables_length').addClass('bs-select');
    $('.request').click((e)=>{
        let id = $(e.target).data('id');
        if (id == undefined)
            id = $(e.target).parent().data('id')
        strHref = location.href.replace('history/', '');
        location.href = strHref + '/requests/' + id;
    });
});