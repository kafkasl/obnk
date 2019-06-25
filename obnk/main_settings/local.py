import os

import psycopg2.extensions
from _base import *

ALLOWED_HOSTS = ["*"]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'obnk_db',
        'USER': 'obnk_usr',
        'PASSWORD': 'obnk_pwd',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

MEDIA_ROOT = "/data/media/"
MEDIA_URL = '/media/'
BASE_URL = 'http://127.0.0.1/'
STATIC_URL = '/static/'
STATIC_ROOT = "/data/static/"
