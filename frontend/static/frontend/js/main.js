// Global scope

var endpointToInputs = {
    systems: ['start_system', 'destination_system'],
    stations: ['start_station', 'destination_station'],
    commodities: ['commodity']
};

var cache = {};
var form = {};

function addToForm(name, item){
    form[name] = item;
}

function matcher(item){
    return this.query.toLowerCase().indexOf(item.name) != -1;
}

function attachInputToModel(name, model){
    var input = '#' + name + '_input';
    var isStation = name.search('station') != -1;

    $(input).typeahead({
        minLength: isStation ? 0 : 2,
        showHintOnFocus: isStation,
        delay: 250, // Millisecond
        source: function(query, process) {
          var requestUrl = '/' + model + '/?search=' + query;

          // If the input is for a station, only supply data from the corresponding system.
          // If no system is selected, return a helper message first.
          if (isStation){
              // Return cached station data for this input if it exists
              if (cache.hasOwnProperty(name)){
                  process(cache[name]);
                  return;
              }

              var correspondingSystemInput = name.replace('station', 'system');
              if (form.hasOwnProperty(correspondingSystemInput)){
                requestUrl = form[correspondingSystemInput].url + 'stations/';
              }
              else{
                process([]);
                return;
              }
            }

            $.getJSON(requestUrl, function(response){
              var autocompleteList = response.data.results;
              if (isStation){
                // Cache the list of station results for this input
                cache[name] = autocompleteList;
              }
              process(autocompleteList);
            });
        },
        afterSelect: function(suggestion){
            addToForm(name, suggestion);
            if (!isStation){
                // Resets the associated station input data cache when a new
                // system is selected.
                var correspondingStationInput = name.replace('system', 'station');
                if (cache.hasOwnProperty(correspondingStationInput)){
                    delete cache[correspondingStationInput];
                }
            }
        }
    });
}

function attachInputsToModels(dict){
    // Attaches the list of inputs from
    for (var model in dict){
        if (dict.hasOwnProperty(model)){
            var input_list = dict[model];
            for (var x = 0; x < input_list.length; x++){
                var input = input_list[x];
                attachInputToModel(input, model);
            }
        }
    }
}

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
    attachInputsToModels(endpointToInputs);

    // When submitting a form, replace inputs with the data in
    // the form variable if it exists.
    $('form').each(function(){
        $(this).submit(function(){
            for (var key in form){
                $('input[name=' + key + ']').val(form[key].url);
            }
        });
    });

    // Default option
    attachSearchToModel('#search_input', 'commodities');

    $(".dropdown-menu li a").click(function(){
        var selText = $(this).text();
        $(this).parents('.input-group').find('input[type=submit]').val(selText);
        attachSearchToModel('#search_input', selText);
    });

    $('#search_form').submit(function(e){
        e.preventDefault();
        var $input = $('#search_input');
        var selected = $input.data('selected');
        if(typeof selected === 'undefined'){
            $('#search_error').html('<div class="alert alert-warning" role="alert">Please select item from dropdown or tab complete.</div>');
        }
        else{
            window.location.href = selected.url;
        }
    });
});