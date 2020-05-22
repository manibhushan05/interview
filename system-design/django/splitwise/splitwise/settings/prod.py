from .base import *

DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0.5/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'splitwisedb',
        'USER': 'mani',
        'PASSWORD': 'whvc.1900',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}