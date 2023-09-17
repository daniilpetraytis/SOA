import os.path

from .common_settings import *

SECRET_KEY = 'django-insecure-mdz!^#-x%yayn!@3(c(=80g9jjmmma=el(#tisa!yzrd9=m^2d'
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = 'static/'

LOGGING['handlers']['file'] = {
    'level': 'DEBUG',
    'class': 'logging.FileHandler',
    'filename': '/tmp/statistics_bo_be.log',
    'formatter': 'verbose'
}

LOGGING['loggers']['django'] = {
    'handlers': ['console'],
    'propagate': True
}

LOG_LEVEL = 'DEBUG' if DEBUG else 'WARNING'


MY_LOGGERS = {}
for app in MY_APPS:
    MY_LOGGERS[app] = {
        'handlers': ['file'],
        'level': LOG_LEVEL,
        'propagate': True,
    }

LOGGING['loggers'].update(MY_LOGGERS)

DEPLOY_MODE = 'local'
