from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    #    '*',
    'grupopac.herokuapp.com',
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
