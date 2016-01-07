[![Build Status](https://travis-ci.org/Jingyu-Yao/elitetraderoutes.svg?branch=master)](https://travis-ci.org/Jingyu-Yao/elitetraderoutes)

www.elitetraderoutes.com

# Project setup
Ryan is cool.

The following setup is for Linux / Windows. Installation scripts are available 
for linux only. All commands should be run in the directory where manage.py is located.

## Required packages

### System packages

#### Linux:

    sudo bash linux_setup.sh

#### Windows:

- python3
- mysql 5.6+ (server only)

### Python packages

#### Linux / Windows:

    pip install -r requirements.txt

## Database settings

Create an user and a database for the user using the settings found in my.cnf file using the following command:

#### Linux:

    bash database_setup.sh

#### Windows:

Open mysql terminal as root@localhost:

    CREATE DATABASE elitetraderoutes CHARACTER SET utf8;
    GRANT ALL PRIVILEGES ON \*.\* TO 'elitetraderoutes'@'localhost' IDENTIFIED BY 'elitetraderoutespassword';

## Additional setup

#### Linux:

    bash project_setup.sh

#### Windows:

    python manage.py migrate
    python manage.py test
    python ingest_data.py
    python manage.py loaddata commodity system station

## Users

You should also create a super user for testing purposes using manage.py

    python manage.py createsuperuser

## EDDN

Start the connection to EDDN:

    python -m eddn.receiver

Licensed under the MIT license.

Copyright © 2015, Jingyu Yao.
All rights reserved.
