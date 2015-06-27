#!/usr/bin/env bash

echo "Don't use this script for production! Define your own db setting and point to it in configs/production.py";
read -s -p "Enter mysql root password: " mysqlpassword
mysql -e "CREATE DATABASE elitetraderoutes CHARACTER SET utf8;" -uroot -p${mysqlpassword}
mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'elitetraderoutes'@'localhost' IDENTIFIED BY 'elitetraderoutespassword';" -uroot -p${mysqlpassword}
echo "Database setup success!"