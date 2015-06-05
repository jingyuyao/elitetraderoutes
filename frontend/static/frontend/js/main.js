// Global scope

// Set up the initial model information by asking for OPTIONS from the api.
// This follows the DRY principal by avoiding hard coding model information in the client.
var models = ['commodity', 'station', 'system', 'connection', 'route']

var systemInputs = ['start_system', 'destination_system']

function attach_search(name, model){
    var input = '#' + name + '_input';
    var span = '#' + name + '_span';

    $(input).keyup(function(){
        $.getJSON('/'+model+'/?search='+$(this).val(), function(data, status){
            $(span).html(JSON.stringify(data));
        });
    });
}

$(document).ready(function(){
    attach_search('start_system', 'system');
    attach_search('destination_system', 'system')
});