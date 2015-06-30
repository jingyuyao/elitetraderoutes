// This file is included on every page. Try not to bloat it.
// Page specific js should be inserted using the script block tag
// from the template.

// Global scope

var cache = {};

function iCompare(search, source){
    return source.toLowerCase().indexOf(search.toLowerCase()) != -1;
}

function findModel(name){
    if (typeof name === 'undefined'){
        return;
    }
    else if (iCompare('system', name)){
        return 'systems';
    }
    else if (iCompare('station', name)){
        return 'stations';
    }
    else if (iCompare('commodity', name)){
        return 'commodities';
    }
}

function attachInputsToModel(){
    $('input').each(function(){
        var $input = $(this);
        var name = $input.attr('name');
        var model = findModel(name);

        if (typeof model === 'undefined'){
            return;
        }

        var isStation = name.search('station') != -1;

        $input.typeahead({
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
                  // We got rid of the id for input tags cause there is no easy way to make them unique across multiple
                  // forms. Now we have to use selectors to find nearest sibling input
                  var selectedSystem = $input.closest('form').find('input[name=' + correspondingSystemInput + ']').data('selected');
                  if (typeof selectedSystem !== 'undefined'){
                    requestUrl = selectedSystem.url + 'stations/';
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
                $input.data('selected', suggestion);
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
    });
}

function showStationCommodities(btn, uuid, station, commodity){
    // Sets up the station commodities div and change button to show/hide the created div
    var $button = $(btn);
    var listId = uuid + '_station_commodities_list';
    $button.after('<div id="' + listId + '" class="collapse"></div>');
    $button.attr('onclick', null);
    $button.attr('data-toggle', 'collapse');
    $button.attr('data-target', '#' + listId);

    populateStationCommoditiesList(listId, station, commodity);
}

function populateStationCommoditiesList(listId, station, commodity, url){
    var $listDiv = $('#'+listId);
    var hasUrl = typeof url !== 'undefined';

    // Get the station commodities
    $.getJSON(hasUrl ? url : '/station_commodities/',
    hasUrl ? null : {
        station: station,
        commodity: commodity
    }, function(data){
        var html = buildStationCommoditiesListNav(data, function(url){
            return 'onclick=\'populateStationCommoditiesList("' + listId + '",null,null,"' + url + '")\'';
        });
        html += buildStationCommoditiesTable(data, station !== null);

        $listDiv.html(html);
    });
}

function buildStationCommoditiesListNav(data, targeter){
    var previous = data.data.previous, next = data.data.next;

    previous = previous ?
        "<li class='previous'><a class='btn' " + targeter(previous) + "><span aria-hidden='true'>&larr;</span> Previous</a></li>"
        : "";

    next = next ?
        "<li class='next'><a class='btn' " + targeter(next) + ">Next <span aria-hidden='true'>&rarr;</span></a></li>"
        : "";

    return '<nav><ul class="pager">' + previous + next + "</ul></nav>";
}

function buildStationCommoditiesTable(data, forStation){
    var results = data.data.results;
    var header = '<table class="table">' + 
                    '<thead>' +
                    '<tr>' +
                        '<th>' + (forStation ? 'Commodity' : 'Station') + '</th>' +
                        '<th>Category</th>' +
                        '<th>Average price</th>' +
                        '<th>Buy</th>' +
                        '<th>Supply (level)</th>' +
                        '<th>Sell</th>' +
                        '<th>Demand (level)</th>' +
                        '<th>Created</th>' +
                    '</tr>' +
                    '</thead>' +
                    '<tbody>';
    var ender =     '</tbody>' +
                '</table>';

    var body = '';

    for (var i = 0; i < results.length; i++) {
        var thing = results[i];

        body += '<tr>';
        body += forStation ? tdAnchorSm(thing.commodity, thing.commodity_name)
                    : tdAnchorSm(thing.station, thing.station_name);
        body += td(thing.category_name);
        body += td(thing.average_price);
        body += td(thing.buy_price);
        body += td(thing.supply + ' (' + thing.supply_level + ')');
        body += td(thing.sell_price);
        body += td(thing.demand + ' (' + thing.demand_level + ')');
        body += td(thing.created);
        body += '</tr>';
    }

    return header + body + ender;
}

function td(thing){
    return '<td>' + thing + '</td>';
}

function tdAnchorSm(url, name){
    return '<td><a class="btn btn-primary btn-sm" href="' + url + '">' + name + '</a></td>';
}

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

    $input.keypress(function(e){
        if (e.which == 13){
            $('#search_error').html('<div class="alert alert-warning" role="alert">Please select item from dropdown or tab complete.</div>');
        }
    });
}

function initSearchBox(){
    // Search box logic
    var $input = $('#search_input');

    // Default option
    var checkedRadio = $('input[name=search_type]:checked');
    attachSearchToModel($input, checkedRadio.val());

    $("input[name=search_type]").click(function(){
        attachSearchToModel($input, $(this).val());
    });
}

function initFormSubmitChange(){
    attachInputsToModel();

    // When submitting a form, replace inputs with input.data('selected').url
    $('form').each(function(){
        var $form = $(this);
        $form.submit(function(){
            $form.find(':input').each(function(){
                var selected = $(this).data('selected');
                if (typeof selected !== 'undefined'){
                    $(this).val(selected.url);
                    $(this).removeData();
                }
            });
        });
    });
}

$(function(){
    initFormSubmitChange();
    initSearchBox();
});
