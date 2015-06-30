#!/usr/bin/env bash

# Requires nodejs, nodejs-legacy, npm, uglifyjs

# It appears apache cache the python process so we need to restart
source ../env/django/bin/activate

git pull
python manage.py collectstatic --noinput

uglifyjs static/frontend/js/main.js --compress --mangle -o static/frontend/js/main.js

sudo service apache2 restart
