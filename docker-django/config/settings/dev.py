"""Development settings and globals."""

from __future__ import absolute_import
from .base import * # noqa

DEBUG = True

# Email host
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thangphuocnguyen.game@gmail.com'
EMAIL_HOST_PASSWORD = 'Halam123abc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# SECRET CONFIGURATION
# SECURITY WARNING: keep the secret key used in production secret!
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tysnblog',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# INSTALLED_APPS += ("debug_toolbar",)

# TASTYPIE SETTINGS --------------------------------

# If set to True and settings.DEBUG = True,
# the standard Django technical 500 is displayed.
TASTYPIE_FULL_DEBUG = True

# Allows your URLs to be missing the final slash
TASTYPIE_ALLOW_MISSING_SLASH = True
