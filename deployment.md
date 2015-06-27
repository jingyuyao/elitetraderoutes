# General deployment guide

Read README.md first!

The deployment process varies greatly depending on the system and a lot of unforeseen factors.

### General process:

- Fresh ubuntu (update, upgrade)
- Install apache2
- Install mod_wsgi (python3 version!)
- Install git (no idea why this isn't default on linux machine)
- Clone repo
- Change settings.py to production mode
- Create and use virtualenv (might need to install python3-virtualenv first)
- Normal project setup by running the scripts
- Collect static files (manage.py collectstatic)
- Config apache2
- Restart apache2

### Links:

- https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/modwsgi/
- https://launchpad.net/ubuntu/trusty/+package/libapache2-mod-wsgi-py3

### Some important thing to note (for ubuntu/debian):

- Use libapache2-mod-wsgi-py3 package for the mod_wsgi to build against python3
- Set the **SECRET_KEY** environment variable (possibly in ~/.profile)

### The apache configuration

Make /etc/apache2/sites-available/elitetraderoutes.conf with the following:

    <VirtualHost *:80>
        ServerName www.elitetraderoutes.com
        WSGIScriptAlias / /home/jingyu/elitetraderoutes/elitetraderoutes/wsgi.py
        WSGIDaemonProcess elitetraderoutes python-path=/home/jingyu/elitetraderoutes:/home/jingyu/env/django/lib/python3.4/site-packages
        WSGIProcessGroup elitetraderoutes
        
        <Directory /home/jingyu/elitetraderoutes/elitetraderoutes>
        <Files wsgi.py>
        Require all granted
        </Files>
        </Directory>
        
        Alias /static/ /home/jingyu/elitetraderoutes/static/
        <Directory /home/jingyu/elitetraderoutes/static>
        Require all granted
        </Directory>
    </VirtualHost>
    
Then enable this virtual host by making a link in the sites-enabled directory:

    cd /etc/apache2/sites-enabled/
    sudo ln -s ../sites-available/elitetraderoutes.conf elitetraderoutes.conf

Of course, change the directories and server names to match your setting.