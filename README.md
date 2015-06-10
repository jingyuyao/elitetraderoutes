[![Build Status](https://travis-ci.org/Jingyu-Yao/elitetraderoutes.svg?branch=master)](https://travis-ci.org/Jingyu-Yao/elitetraderoutes)
# Project setup

The following setup is Linux / Windows

## Required packages

### System packages

Linux:

sudo bash linux_setup.sh

Windows:

- python3
- mysql 5.6+ (server only)

### Python packages

pip install -r requirements.txt

## Database settings

Create an user and a database for the user using the settings found in my.cnf file using the following command:

Linux:

bash database_setup.sh

Windows:

Open mysql terminal as root@localhost:

- CREATE DATABASE elitetraderoutes CHARACTER SET utf8;
- GRANT ALL PRIVILEGES ON \*.\* TO 'elitetraderoutes'@'localhost' IDENTIFIED BY 'elitetraderoutespassword';

## Additional setup

Linux:

bash project_setup.sh

Windows:

### Populate the database with models and run tests

- python manage.py migrate
- python manage.py test

### Download data from eddb.io and load into database

- python ingest_data.py
- python manage.py loaddata commodity system station
