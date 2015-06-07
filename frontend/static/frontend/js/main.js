// Global scope

var modelToInputs = {
    system: ['start_system', 'destination_system'],
    station: ['start_station', 'destination_station'],
    commodity: ['commodity']
};

var form = {};

function addToForm(item){
    if (item.hasOwnProperty('name')){
        form[item.name] = item;
    }
}

function createAutocompleteList(results, name, model){
    var list = [];

    $.each(results, function(i, val){
        var data = {
            value: val.name,
            label: val.name,
            url: val.url,
            name: name,
            model: model
        };
        list.push(data);
    });

    return list;
}

function attachInputToModel(name, model){
    var input = '#' + name + '_input';

    $(input).autocomplete({
        minLength: 2,
        source: function(req, add) {
            var requestUrl = '/'+model+'/?search='+req.term;

            // If the input is for a station, only supply data from the corresponding system.
            // If no system is selected, return a helper message first.
            if (name.search('station') != -1){
                var correspondingSystemInput = name.replace('station', 'system');
                if (form.hasOwnProperty(correspondingSystemInput)){
                    requestUrl = form[correspondingSystemInput].url + 'stations/';
                }
                else{
                    add(['Please select a system first.']);
                    return;
                }
            }

            $.getJSON(requestUrl, function(data){
                var autocompleteList = createAutocompleteList(data.data.results, name, model);
                add(autocompleteList);
            });
        },
        select: function(event, ui){
            addToForm(ui.item);
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

$(function(){
    attachInputsToModels(modelToInputs);

    // When submitting a form, replace inputs with the data in
    // the form variable if it exists.
    $('form').each(function(){
        $(this).submit(function(){
            for (var key in form){
                $('input[name=' + key + ']').val(form[key].url);
            }
        });
    });
});