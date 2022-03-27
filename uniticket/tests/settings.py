"""
Django settings for uni_ticket_project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import pathlib

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rz82a_#y1#s=l+loeqgn_4xslwchu%yxtpdf)h7b$6kn+p+=+^'

from . settingslocal import * # noqa: F401

# load applications settings file, overload what needed if needed
from django_form_builder.settings import * # noqa: F401
from organizational_area.settings import * # noqa: F401

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOME_PAGE = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
DATA_DIR = os.path.join(BASE_DIR, "data")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
if not os.path.exists(STATIC_ROOT):
    pathlib.Path(STATIC_ROOT).mkdir(parents=True, exist_ok=True)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    pathlib.Path(MEDIA_ROOT).mkdir(parents=True, exist_ok=True)

# used for pdf creation and other temporary files
CACHE_DIR='uni_ticket_project_cache'
TMP_DIR = os.path.sep.join((BASE_DIR, CACHE_DIR, 'tmp'))
if not os.path.exists(TMP_DIR):
    pathlib.Path(TMP_DIR).mkdir(parents=True, exist_ok=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uni_ticket_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

WSGI_APPLICATION = 'uni_ticket_project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "accounts.User"
LOCAL_URL_PREFIX = 'local'
LOGIN_URL = f'/{LOCAL_URL_PREFIX}/login/'
LOGOUT_URL = f'/{LOCAL_URL_PREFIX}/logout/'

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATETIME_FORMAT = '{} %H:%M'.format(DEFAULT_DATE_FORMAT)
DATE_INPUT_FORMATS = [DEFAULT_DATE_FORMAT, '%d/%m/%Y']

# This parameters define the roles of users to open ticket
# If True, an employee is a user that has this parameter filled (in user model)
# If False, an employee is a user that is mapped as OrganizationalStructureOfficeEmployee
EMPLOYEE_ATTRIBUTE_NAME = 'matricola_dipendente'
# If True, an internal user (not guest) is a user that has this filled (in user model)
# If False, an internal user is a user that is mapped as OrganizationalStructureOfficeEmployee
USER_ATTRIBUTE_NAME = 'matricola_studente'

SIMPLE_USER_SHOW_PRIORITY = False

# from django 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
