"""Development settings and globals."""

from __future__ import absolute_import
from .base import *

DEBUG = True

# Email host
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thangphuocnguyen.game@gmail.com'
EMAIL_HOST_PASSWORD = 'Halam123abc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')6ohywwb&^u@1#ed-2fcc#452$$ubj93w$e+2gd29+6puccj1y'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
