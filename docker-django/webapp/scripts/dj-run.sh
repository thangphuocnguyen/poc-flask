#!/bin/sh

pip install -r requirements/local.txt
python manage.py runserver 0.0.0.0:8000
