$(document).ready(function () {
    $('#dtBasicExample').DataTable();
    $('#dtBasicExamplePast').DataTable();
    $('.dataTables_length').addClass('bs-select');

    $('body').on('click', '.request', (e) => {
    //$('.request').click((e)=>{
        let walker_id = $(e.target).data('walker_id');
        if (walker_id != undefined){
            strHref = "http://localhost:5000/"
            window.location.href = strHref + 'walkerShow/' + walker_id;
        }
        else{ 
            let id = $(e.target).data('id');
            if (id == undefined)
                id = $(e.target).parent().data('id')
            strHref = location.href.replace('history/', '');
            location.href = strHref + '/requests/' + id;
        }
    });


    $('body').on('click', '.requestPast', (e) => {

        let id = $(e.target).data('id');
        let pet_id = $(e.target).data('pet_id');
        let walker_id = $(e.target).data('walker_id');
        strHref = "http://localhost:5000/"
        if (walker_id != undefined)
            window.location.href = strHref + 'walkerShow/' + walker_id;
        else{ 
            if (id == undefined)
                id = $(e.target).parent().data('id')
            if (pet_id == undefined)
                pet_id = $(e.target).parent().data('pet_id')
            window.location.href = strHref + 'pets/' + pet_id + '/requests/' + id;
        }
    });
});