#!/bin/sh

pip install -r requirements/local.txt
/usr/local/bin/gunicorn djangoprj.config.wsgi:application -w 2 -b :8000
