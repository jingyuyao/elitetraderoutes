// Global scope

var endpointToInputs = {
    systems: ['start_system', 'destination_system'],
    stations: ['start_station', 'destination_station'],
    commodities: ['commodity']
};

var form = {};

var typeaheadSetting = {
    hint: true,
    highlight: true,
    minLength: 2
}

function addToForm(name, item){
    form[name] = item;
}

function attachInputToModel(name, model){
    var input = '#' + name + '_input';

    $(input).typeahead(typeaheadSetting, {
        name: name,
        display: 'name',
        source: function(query, sync, async) {
            // Local data use sync callback and remote data use async callback

           var requestUrl = '/' + model + '/?search=' + query;

           // If the input is for a station, only supply data from the corresponding system.
           // If no system is selected, return a helper message first.
           if (name.search('station') != -1){
               var correspondingSystemInput = name.replace('station', 'system');
               if (form.hasOwnProperty(correspondingSystemInput)){
                   requestUrl = form[correspondingSystemInput].url + 'stations/';
               }
               else{
                   sync([{name:"Please select a system first."}]);
                   return;
               }
           }

           $.getJSON(requestUrl, function(response){
                var autocompleteList = response.data.results;
                if (requestUrl.search('station') != -1){
                   var reqLower = query.toLowerCase();

                   autocompleteList = autocompleteList.filter(function(element){
                       var eleLower = element.name.toLowerCase();
                       return eleLower.search(reqLower) != -1;
                   });
                }
                async(autocompleteList);
           });
       }
    }).on('typeahead:select typeahead:autocomplete', function(ev, suggestion){
        addToForm(name, suggestion);
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
});