// Global scope

var modelToInputs = {
    'system': ['start_system', 'destination_system'],
    'station': ['start_station', 'destination_station'],
    'commodity': ['commodity']
};

var modelCache = {};

// Sync model info from modelToInputs to nameToUrlCache
for (var key in modelToInputs){
    modelCache[key] = [];
}

console.log(modelCache);

function addToCache(instance, model){
    var nameToUrlPairing = {
        'name': instance.name,
        'url': instance.url
    };

    modelCache[model].push(nameToUrlPairing);

    return nameToUrlPairing;
}

function attachInputToModel(name, model){
    var input = '#' + name + '_input';
    var span = '#' + name + '_span';

    $(input).keyup(function(){
        $.getJSON('/'+model+'/?search='+$(this).val(), function(data, status){
            var results = data['data']['results'];
            var names = [];

            for (var i = 0; i < results.length; i++){
                var nameToUrl = addToCache(results[i], model);
                names.push(nameToUrl['name']);
            }

            $(span).html(names.toString());
        });
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

$(document).ready(function(){
    attachInputsToModels(modelToInputs)
});