"""
Django settings for FirstApp project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6xxjk@29s+j0h8q7^il@0!lpv(zxpe3s6ozo4vaj@9s!d(-(p3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'travello.apps.TravelloConfig', #necessary for letting the project know what apps its working with. used for migrations and templates
    'destinations.apps.DestinationsConfig',
    'accounts.apps.AccountsConfig',
    #'djangobower',
    #'schedule.apps.ScheduleConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'FirstApp.urls'
LOGIN_URL = '/accounts/login/' #for using login required decorator

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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


WSGI_APPLICATION = 'FirstApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'FirstApp', #name of the databse we created
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost', #specify which machine has the database
        'PORT': '5432',
    
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images, "plugins", "styles", etc.)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

"""
BOWER_INSTALLED_APPS = (
    'jquery',
    'jquery-ui',
    'bootstrap'
)
STATICFILES_FINDERS = [
    'djangobower.finders.BowerFinder',
]
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
"""

STATIC_URL = '/static/' #how we will get to static files from within templates

STATICFILES_DIRS = [ #a list of directories where Django will look for static files to use
    os.path.join(BASE_DIR, "static/FirstApp"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')  #lets Django put all the static files it finds into its own folder called assets
                                                #must call " python manage.py collectstatic " to create an assets folder

MEDIA_URL = '/media/'  #how we get to media files from within templates

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  #specify location of media files (the folder)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'