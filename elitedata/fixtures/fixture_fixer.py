#!/usr/bin/env python
import json

__author__ = 'jingyu'

APP_NAME = 'elitedata'

def fix_fixture(directory, file, model_name):
    """
    Changes the data downloaded from eddb.io into django fixture format.

    This function is tailored specifically for data in the unfixed directory
    so it should not be used elsewhere.

    :param file:
    :param model_name:
    :return:
    """

    with open(directory + file) as input, open(directory + model_name+".json", mode="wt") as output:
        objects = json.load(input)

        for obj in objects:
            # Each object in the django fixture need a model name and pk
            obj['model'] = '%s.%s' % (APP_NAME, model_name)
            obj['pk'] = obj.pop('id')

            # The actual data of the model goes into a 'fields' attribute
            fields = {}

            # Get a copy of the keys attribute so we can safely get rid of
            # keys in a loop without
            keys = list(obj.keys())

            # Moving all the data fields from the object into 'fields'
            for key in keys:
                if key not in ('model', 'pk'):
                    value = obj.pop(key)
                    # We don't keep any field with an array as value to save the hassle
                    # of making JOIN tables.
                    if type(value) is list:
                        continue
                    # Flatten out the inner fields if value is a dict
                    # Nested fields occurs for commodities.json
                    elif type(value) is dict:
                        for nkey in value.keys():
                            # Assume nesting only goes one layer down and
                            # contains no arrays.
                            fields['%s_%s' % (key, nkey)] = value[nkey]
                    else:
                        # Manual fix for system_id_id problem
                        if key == 'system_id':
                            fields['system'] = value
                        else:
                            fields[key] = value

            # Put all data fields under a fields attribute of the object
            obj['fields'] = fields

        json.dump(objects, output, indent=2)

def fix_all(fixture_directory):
    fix_fixture(fixture_directory, "commodities.json", 'commodity')
    fix_fixture(fixture_directory, "stations_lite.json", 'station')
    fix_fixture(fixture_directory, "systems.json", "system")
