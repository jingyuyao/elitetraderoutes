function attachSearchToModel(id, model){
    var $input = $(id);

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
            $input.data('selected', suggestion);
        }
    });
}

$(function(){
    // Search box logic
    // Default option
    attachSearchToModel('#search_input', 'commodities');

    $(".dropdown-menu li a").click(function(){
        var selText = $(this).text();
        $(this).parents('.input-group').find('input[type=submit]').val(selText);
        attachSearchToModel('#search_input', selText);
    });

    var $search_form = $('#search_form');

    $search_form.off('submit'); // Need to get rid of previously defined handler first
    $search_form.submit(function(e){
        e.preventDefault();
        var $input = $('#search_input');
        var selected = $input.data('selected');
        if(typeof selected === 'undefined'){
            $('#search_error').html('<div class="alert alert-warning" role="alert">Please select item from dropdown or tab complete.</div>');
        }
        else{
            $input.removeData();
            window.location.href = selected.url;
        }
    });
});