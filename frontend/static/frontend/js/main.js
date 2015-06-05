$(document).ready(function(){
    function get_json(url_, callback){
        $.ajax({
            url: url_,
            type: "GET",
            accept: "application/json",
            success: callback
        });
    }

    $("#start_system_input").keyup(function(){
        get_json("/systems/?search=" + $(this).val(), function(data, status){
           $('#start_system_span').html(JSON.stringify(data));
        });
    });
});