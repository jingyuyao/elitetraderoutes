#!/usr/bin/env bash

# Yep you guessed it!
git pull
python manage.py collectstatic --noinput
