$(document).ready(function(){
    function get_json(url_, callback){
        $.ajax({
            url: url_,
            type: "GET",
            accept: "application/json",
            success: callback
        });
    }

    $("#route_input").keyup(function(){
        get_json("/routes/", function(data, status){
           alert(JSON.stringify(data));
        });
    });
});