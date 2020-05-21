from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0.5/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'udaandb',
        'USER': 'mani',
        'PASSWORD': 'whvc.1900',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
