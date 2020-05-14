"""
Django settings for darpana project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import re

import django_heroku

POSTGRES_URL_REGEX = re.compile(
    r'^postgres:\/\/(?P<username>.*?):(?P<password>.*?)@(?P<host>.*?):(?P<port>\d+)/(?P<db>.*?)$')


def get_postgres_settings(url):
    matches = POSTGRES_URL_REGEX.match(url)
    return {
        'name': matches.group('db'),
        'username': matches.group('username'),
        'password': matches.group('password'),
        'host': matches.group('host'),
        'port': matches.group('port')
    }


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'test')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'stormy-ravine-65597.herokuapp.com',
    'localhost',
    '127.0.0.1'
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:4200",
    "http://127.0.0.1:8000"
]

# Application definition

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig',
    'blog.apps.BlogConfig',
    'userview.apps.UserviewConfig',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'darpana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dashboard.context_processors.return_category_details',
            ],
        },
    },
]

WSGI_APPLICATION = 'darpana.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
pg = get_postgres_settings(os.environ.get('DATABASE_URL', 'postgres://hamsadatta:password@127.0.0.1:5432/darpana'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': pg['name'],
        'USER': pg['username'],
        'PASSWORD': pg['password'],
        'HOST': pg['host'],
        'PORT': pg['port'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = 'whitenoise.django.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "dist"),
]

django_heroku.settings(locals())
