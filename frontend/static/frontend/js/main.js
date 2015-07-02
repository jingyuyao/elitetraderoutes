// This file is included on every page. Try not to bloat it.
// Page specific js should be inserted using the script block tag
// from the template.

// Global scope

var cache = {};
var STATIC_BASE = '/static/frontend/';

function showStationCommodities(btn, uuid, station, commodity){
    // Change button to show/hide the created div
    var $button = $(btn);
    var listId = uuid + '_station_commodity_list';
    $button.closest('p').after('<div class="collapse" id="' + listId + '"></div>');
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
        var forStation = station !== null;
        var html = "";

        $.get(STATIC_BASE + 'templates/list_nav.mustache').done(function(template){
            html += Mustache.render(template, {
                previous: data.data.previous,
                next: data.data.next,
                targeter: function(){
                    return function(val, render){
                        // The cursor style is a hack for pager with no href
                        return 'style="cursor: pointer;" onclick=\'populateStationCommoditiesList("' + listId + '",' + station + ',' + commodity + ',"' + render(val) + '");\'';
                    }
                }});
        }).always(function(){
            $.get(stationCommodityTemplateChooser(forStation)).done(function(template){
                html += Mustache.render(template, data);
                $listDiv.html(html);
            });
        });
    });
}

function stationCommodityTemplateChooser(forStation) {
    return STATIC_BASE + (forStation ? 'templates/station_commodities_table.mustache'
                                     : 'templates/commodity_stations_table.mustache');
}

function initSearchBox(){
    // Search box logic
    var $input = $('#search_input');

    if (!$input.length) {
        return;
    }

    // Default option
    var checkedRadio = $('input[name=search_type]:checked');
    attachSearchToModel($input, checkedRadio.val());

    $("input[name=search_type]").click(function(){
        attachSearchToModel($input, $(this).val());
    });
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

function initFormSubmitChange(){
    var $forms = $('form');

    if (!$forms.length) {
        return;
    }

    // When submitting a form, replace inputs with input.data('selected').url
    $forms.each(function(){
        var $form = $(this);

        attachTypeaheadForInputs($form);

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

function attachTypeaheadForInputs($form){
    $form.find(':input').each(function(){
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

function initStationCommoditySearchBox(){
    var $inputs = $('input[name=station_commodity_search_input]');

    if (!$inputs.length) {
        return;
    }

    $inputs.each(function(){
        var $input = $(this);
        var resultsDivId = $input.data('uuid') + '_station_commodity_results';
        $input.closest('p').after('<div class="collapse" id="' + resultsDivId + '"></div>');
        var $resultsDiv = $('#' + resultsDivId);
        var forStation = $input.data('station') !== undefined;

        $input.keypress(function(e){
            if (e.which == 13){
                var val = $input.val();

                if (val.length < 2) {
                    $resultsDiv.html('<p>Minimum of 2 characters to search</p>');
                }
                else {
                    $.getJSON('/station_commodities/', {
                        commodity: $input.data('commodity'),
                        station: $input.data('station'),
                        search: val
                    }, function(data){
                        if (data.data.count) {
                            $.get(stationCommodityTemplateChooser(forStation)).done(function(template){
                                $resultsDiv.html(Mustache.render(template, data));
                            });
                        }
                        else {
                            $resultsDiv.html('<p>No results</p>');
                        }
                    });
                }
                $resultsDiv.collapse('show');
            }
        });
    });
}

$(function(){
    initFormSubmitChange();
    initSearchBox();
    initStationCommoditySearchBox();
});
