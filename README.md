# Project setup

The following setup is for Linux Ubuntu/Mint

## Required packages

### System packages

- python3
- python3-dev
- mysql-server
- mysql-client
- libmysqlclient-dev

### Python packages

- pip
- setuptools
- Django
- mysqlclient
- rest_framework

## Database settings

Create an user and a database for the user using the settings found in my.cnf file using the following command:

As root@localhost:

- CREATE DATABASE elitetraderoutes CHARACTER SET utf8;
- GRANT ALL PRIVILEGES ON elitetraderoutes.* TO 'elitetraderoutes'@'localhost' IDENTIFIED BY 'elitetraderoutespassword';

Then run 'python3 manage.py migrate' and make sure there are no errors.

## User settings

### Required users

Keep these users' passwords a secret.

- admin
- guest
