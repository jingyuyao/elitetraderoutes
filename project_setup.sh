#!/usr/bin/env bash

echo "Migrating.."
python manage.py migrate
echo "Testing..."
python manage.py test
echo "Download and fixing data..."
python ingest_data.py
echo "Loading data to database..."
python manage.py loaddata commodity system station