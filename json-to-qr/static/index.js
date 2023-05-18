$("#form").submit(function(e){
    e.preventDefault();
});

function pretty_print() {
    var ugly = document.getElementById('json_data').value;
    var obj = JSON.parse(ugly);
    var pretty = JSON.stringify(obj, undefined, 4);
    document.getElementById('json_data').value = pretty;
}

function send_ajax_request(){
    let data = $('#json_data').val();
    $('#form')[0].reset();
    $('#qr_data').val(data);
    $.ajax({
        type : 'POST',
        url : '',
        data : {'csrfmiddlewaretoken': csrf , 'json_data': data ,'action':'qr_code'},
        success : function (result) {
            console.log(result.file_name);
            let qr_image = document.getElementById('qr-img'); 
            qr_image.setAttribute('src',media+result.file_name);
            qr_image.style.display = 'block';
        }
    })
}