# Django deployment notes

## Gunicorn

*Install gunicorn via pip*

`$ pip install gunicorn`

*Create bin/gunicorn_start script to configure the gunicorn* 

	refer to bin/gunicorn for more details

## Nginx

*Install and start nginx*

`$ sudo apt-get install nginx`

`$ sudo service nginx start`

*Describe Nginx server config in the /etc/nginx/sites-available directory.*

	Refer to current config as an example in doc/simlledjangoprj.nginx.conf

*Create an Nginx virtual server configuration for Django*

`$ sudo vim /etc/nginx/sites-available/<server-name>`

*Enable site by making symbolic links to configuration file in the /etc/nginx/sites-enabled directory.*

`$ sudo ln -s /etc/nginx/sites-available/<server-name> /etc/nginx/sites-enabled/<server-name>`

*Recheck the nginx configuration syntax*

`$ sudo nginx -t `

*Restart Nginx to update configuration*

`$ sudo service nginx restart `

## Others notes:

*Run collects static to update static directory*

`$ python manage.py collectstatic`

*Check the nginx error log by using*

`$ sudo tail -30 /var/log/nginx/error.log`


## References:
[http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/](http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/)

