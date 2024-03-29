"""
Django settings for chider project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')


LOCAL = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if LOCAL:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['luach-belz.ew.r.appspot.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'luach',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'chider.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chider.wsgi.application'



if LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:

    import pymysql  # noqa: 402
    pymysql.version_info = (1, 4, 6, 'final', 0)  # change mysqlclient version
    pymysql.install_as_MySQLdb()

    # [START db_setup]
    if os.getenv('GAE_APPLICATION', None):
        # Running on production App Engine, so connect to Google Cloud SQL using
        # the unix socket at /cloudsql/<your-cloudsql-connection string>
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '/cloudsql/luach-belz:europe-west1:belz-luach1',
                'NAME': 'main',
                'USER': 'root',
                'PASSWORD': 'David5006',
            }
        }
    else:
        # Running locally so connect to either a local MySQL instance or connect to
        # Cloud SQL via the proxy. To start the proxy via command line:
        #
        #     $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306
        #
        # See https://cloud.google.com/sql/docs/mysql-connect-proxy
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'HOST': '/cloudsql/luach-belz:europe-west1:belz-luach1',
                'PORT': '3306',
                'NAME': 'main',
                'USER': 'root',
                'PASSWORD': 'David5006',
            }
        }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'Europe/Brussels'

TIME_INPUT_FORMATS = [
    '%H:%M',        # '14:30'
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
]

USE_I18N = True

USE_L10N = True

USE_TZ = True

#DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#GS_BUCKET_NAME = 'luach-belz'
#STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#GS_FILE_OVERWRITE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

if LOCAL:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

else:

    STATIC_URL = 'https://storage.googleapis.com/luach-belz/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#MEDIA_URL = 'https://storage.googleapis.com/luach-belz/static/images/'
#MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
from google.oauth2 import service_account
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR,'credentials.json'))


DEFAULT_FILE_STORAGE='chider.gcloud.GoogleCloudMediaFileStorage'
GS_PROJECT_ID = 'luach-belz'
GS_BUCKET_NAME = 'luach-belz'
MEDIA_ROOT = "media/"
UPLOAD_ROOT = 'media/uploads/'
MEDIA_URL = 'https://storage.googleapis.com//{}/'.format(GS_BUCKET_NAME)


INTERNAL_IPS = ['127.0.0.1']
