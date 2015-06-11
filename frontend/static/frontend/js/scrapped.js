// NEVER DELETE CODE!

// Old jQuery-ui autocomplete version
//function attachInputToModel(name, model){
//    var input = '#' + name + '_input';
//
//    $(input).autocomplete({
//        minLength: 2,
//        source: function(req, add) {
//
//            var requestUrl = '/'+model+'/?search='+req.term;
//
//            // If the input is for a station, only supply data from the corresponding system.
//            // If no system is selected, return a helper message first.
//            if (name.search('station') != -1){
//                var correspondingSystemInput = name.replace('station', 'system');
//                if (form.hasOwnProperty(correspondingSystemInput)){
//                    requestUrl = form[correspondingSystemInput].url + 'stations/';
//                }
//                else{
//                    add(['Please select a system first.']);
//                    return;
//                }
//            }
//
//            $.getJSON(requestUrl, function(data){
//                var autocompleteList = createAutocompleteList(data.data.results, name, model);
//                if (requestUrl.search('station') != -1){
//                    var reqLower = req.term.toLowerCase();
//
//                    autocompleteList = autocompleteList.filter(function(element){
//                        var eleLower = element.value.toLowerCase();
//                        return eleLower.search(reqLower) != -1;
//                    });
//                }
//                add(autocompleteList);
//            });
//        },
//        select: function(event, ui){
//            addToForm(ui.item);
//        }
//    });
//}
//
// function createAutocompleteList(results, name, model){
//     var list = [];

//     $.each(results, function(i, val){
//         var data = {
//             value: val.name,
//             label: val.name,
//             url: val.url,
//             name: name,
//             model: model
//         };
//         list.push(data);
//     });

//     return list;
// }