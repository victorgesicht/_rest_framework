
from pathlib import Path
from configurations import Configuration, values
import sys
import os



#no logger needed cause of django_crispy_logging


class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent

    TAILWIND_APP_NAME = 'tailwindFfs'
    SECRET_KEY = 'django-insecure-fw0gc!b7jjgloxwg)-6(#s8_%3e#mxx-0o8!nu*d9^4^#$8oht'

    DEBUG=True
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent





    ALLOWED_HOSTS =['127.0.0.1', 'localhost']
            #PARSING conf-vars

            #bool vars,secretvals,
            #NOTE:FALSE not 'false' or '0' are considered True---
            #for secret vals, if not found, a random one is generated and used.
            #####otherwise,SECRET_KEY=values.SecretValue(),not.secretval('default_key_here')
            #SO WHERE IS THE VALUE STORED? ENV VARIABLES OR A .env FILE. example for secret key:
            #export DJANGO_SECRET_KEY='your_secret_key_here'
            # List values to make appendlist arrays easier i.e the allowed hosts variable.
            #for db_values:import dj_database_url, db_schema,
            #






    # Application definition

    INSTALLED_APPS = [
        'django_daisy',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'c3App',
        'rest_framework',
        'crispy_bootstrap5',
        'django.contrib.humanize',
        'tailwindFfs',



        ###'django_filters',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'c3.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'static'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'c3.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/5.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/5.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.2/howto/static-files/

    STATIC_URL = 'static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'


    # Default primary key field type
    # https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    DJANGO_CONFIGURATION = 'Dev'
    DJANGO_SETTINGS_MODULE = 'c3.settings'
    CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'  # or your chosen one
    CRISPY_TEMPLATE_PACK = 'bootstrap5'
    AUTH_USER_MODEL = 'c3App.DefaultUser'

    #logging can be done anywhere in the code since logging import is globally accessible.
    #best done in the settings .py: centralizing configs,clean and logging at startup.

    LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },

    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose", "level": "INFO", "stream": "ext://sys.stdout"},
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "level": "DEBUG",
            "filename": "app.log",
            "maxBytes": 5_000_000,
            "backupCount": 5,
            "encoding": "utf8"
        }
    },

    "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }



class Prod(Dev):
    DEBUG = False
    SECRET_KEY=values.SecretValue()
    ALLOWED_HOSTS= values.ListValue(['9t6-production.up.railway.app'])