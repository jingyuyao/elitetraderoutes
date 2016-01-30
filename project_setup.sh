#!/usr/bin/env bash

echo "Migrating.."
python manage.py migrate
echo "Testing..."
python manage.py test
# EDDB changed their data layout so it is incompatible with our existing database :(
# echo "Download and fixing data..."
# python ingest_data.py
# echo "Loading data to database..."
# python manage.py loaddata commodity system station
