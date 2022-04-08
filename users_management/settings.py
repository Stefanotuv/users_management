"""
Django settings for users_management project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# import pymysql
#
# pymysql.install_as_MySQLdb()

# import rest_framework_simplejwt

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j71t+kmuk*bo0f85@8y*#bll)apizup&yoh0(y99sl6(e-c^sx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','192.168.0.165']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # added to create user and profile
    'allauth',
    'allauth.account',
    'django.contrib.sites',
    'users.apps.UsersConfig',
    'crispy_forms',

    # added to prevent errors on API
    'corsheaders',

    # to be understood when to use for auth
    # 'rest_framework_simplejwt',

    'gentelelladjango',

    'grouping',

]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
#
# }

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # added to prevent API errors
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'users_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',
                 # replace the previous user template to force the use the login template on grouping
                 os.path.join(BASE_DIR, 'grouping/users/templates'),

                 # old
                 # os.path.join(BASE_DIR, 'users/templates'),
                 # os.path.join(BASE_DIR, 'users'),

                 # the order is important if there is an overalaps of names
                 os.path.join(BASE_DIR, 'grouping/templates'),
                 os.path.join(BASE_DIR, 'grouping'),
                 os.path.join(BASE_DIR, 'grouping/templates/grouping'),

                 os.path.join(BASE_DIR, 'gentelelladjango/templates'),
                 os.path.join(BASE_DIR, 'gentelelladjango'),
                 ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
            'libraries': {
                'get_item': 'grouping.templatetags.get_item',

            },
        },
    },
]

WSGI_APPLICATION = 'users_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# sqllite (working)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# mysql test connection
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': BASE_DIR / 'user_management/mysql.cnf',
#         },
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'usermanagement',
#         'USER': 'user',
#         'PASSWORD': 'Pinocchi0',
#         'HOST': '192.168.0.118',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# added to use the custom user model
AUTH_USER_MODEL = 'users.User'

# added to send to profile after login-in. this should be updated if the page has to be the home page post login
LOGIN_REDIRECT_URL = 'home' # OLD VERSION the login pages have been moved
LOGIN_URL = 'users_login'

# added
MEDIA_ROOT = os.path.join(BASE_DIR, 'users','media')
# MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/users/media/'

# added to prevent API errors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# no limit to the number of parameters on get and post
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 0
DEFAULT_FROM_EMAIL = 'Grouping Project Admin'