from os import getenv

ENV = getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'

SECRET_KEY = getenv('SECRET_KEY')