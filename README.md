# Project setup

The following setup is Linux / Windows

## Required packages

### System packages

- python3
- mysql 5.6+ (server only) (windows)
- python3-dev (linux)
- mysql-server (linux)
- mysql-client (linux)
- libmysqlclient-dev (linux)

### Python packages

- pip
- setuptools
- django
- django-filter
- mysqlclient
- rest_framework
- requests

## Database settings

Create an user and a database for the user using the settings found in my.cnf file using the following command:

As root@localhost:

- CREATE DATABASE elitetraderoutes CHARACTER SET utf8;
- GRANT ALL PRIVILEGES ON elitetraderoutes.* TO 'elitetraderoutes'@'localhost' IDENTIFIED BY 'elitetraderoutespassword';

Then run 'python3 manage.py migrate' and make sure there are no errors.

## Additional setup

Run elitedata/fixtures/ingest_data.py
Then run manage.py loaddata commodity system station