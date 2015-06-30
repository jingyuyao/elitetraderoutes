#!/usr/bin/env bash

# It appears apache cache the python process so we need to restart
git pull
python manage.py collectstatic --noinput
sudo service apache2 restart