function attachSearchToModel($input, model){
    // Clean previous typeahead
    $input.typeahead('destroy');

    $input.typeahead({
        minLength: 2,
        delay: 250, // Millisecond
        source: function(query, process) {
            var requestUrl = '/' + model + '/?search=' + query;

            $.getJSON(requestUrl, function(response){
                process(response.data.results);
            });
        },
        afterSelect: function(suggestion){
            window.location.href = suggestion.url;
        },
        displayText: function(item){
            if (item.hasOwnProperty('system_name')){
                return item.name + ' (' + item.system_name + ')';
            }

            return item.name;
        }
    });
}

$(function(){
    // Search box logic
    var $input = $('#search_input'), $btn = $('#search_input_btn');

    // Default option
    attachSearchToModel($input, 'commodities');

    $(".dropdown-menu li a").click(function(){
        var selText = $(this).text();
        $btn.html(selText+'<span class="caret"></span>');
        attachSearchToModel($input, selText);
    });

    $input.keypress(function(e){
        if (e.which == 13){
            $('#search_error').html('<div class="alert alert-warning" role="alert">Please select item from dropdown or tab complete.</div>');
        }
    });
});