#!/usr/bin/env bash

# Requires nodejs, npm, uglifyjs

# It appears apache cache the python process so we need to restart
git pull
python manage.py collectstatic --noinput

uglifyjs /static/frontend/js/main.js -o /static/frontend/js/main.js

sudo service apache2 restart