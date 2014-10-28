"""
Django settings for treasurehunt project.

"""

import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ON_PAAS = 'OPENSHIFT_REPO_DIR' in os.environ

if ON_PAAS:
    SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
else:
    SECRET_KEY = ')_7av^!cy(wfx=k#3*7x+(=j^fzv+ot^1@sh9s9t=8$bu@r(z$'


# Adjust to turn off when on Openshift, but allow an environment variable to override on PAAS
DEBUG = not ON_PAAS
DEBUG = DEBUG or 'DEBUG' in os.environ
if ON_PAAS and DEBUG:
    print("*** Warning - Debug mode is on ***")

TEMPLATE_DEBUG = True

if ON_PAAS:
    ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS'], socket.gethostname()]
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'treasure_hunt',
    'registration',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'treasurehunt.urls'

WSGI_APPLICATION = 'treasurehunt.wsgi.application'


# Database settings

if ON_PAAS:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  
            'NAME':     os.environ['OPENSHIFT_APP_NAME'],
            'USER':     os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
            'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
            'HOST':     os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
            'PORT':     os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
        }
    }
else:
    # Database for testing locally
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi/static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'wsgi/media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Django-Registration settings
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
