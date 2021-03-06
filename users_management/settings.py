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
import dotenv

# https://www.oracle.com/database/technologies/instant-client/downloads.html
# https://blogs.oracle.com/opal/post/how-to-connect-to-oracle-autonomous-cloud-databases
# https://blogs.oracle.com/opal/post/connecting-to-oracle-cloud-autonomous-database-with-django
import cx_Oracle


# import pymysql
#
# pymysql.install_as_MySQLdb()

# import rest_framework_simplejwt

# Build paths inside the project like this: BASE_DIR / 'subdir'.




BASE_DIR = Path(__file__).resolve().parent.parent



dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
if os.environ['ENVIRONMENT'] =='prod':
    if os.environ['PROCESSOR'] == 'ARM':
        cx_Oracle.init_oracle_client(lib_dir="/home/ubuntu/project_grouping/connect/instantclient_19_10",config_dir="/home/ubuntu/project_grouping/connect/instantclient_19_10/network/admin")
    else:
        cx_Oracle.init_oracle_client(lib_dir="/home/ubuntu/project_grouping/connect/instantclient_21_5")
elif os.environ['ENVIRONMENT'] =='test':
    cx_Oracle.init_oracle_client(lib_dir="/Users/stefano/Dropbox/NewDev/user_management_connect")
else:
    # do nothing as in dev the app uses sqlite to make testing easier
    pass


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

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
if os.environ['ENVIRONMENT'] =='prod':
    SITE_ID = 4
elif os.environ['ENVIRONMENT'] =='test':
    SITE_ID = 4
elif os.environ['ENVIRONMENT'] =='dev':
    SITE_ID = 2
else:
    pass


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
                 os.path.join(BASE_DIR, 'grouping/templates/users'),

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
# DATABASES = {
#     'default': {
#         'ENGINE':  os.environ['ENGINE'],
#         'NAME':  BASE_DIR/'db.sqlite3',
#     }
# }


# mysql test connection
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': BASE_DIR / 'user_management/mysql.cnf',
#         },
#     }
# }

if os.environ['ENVIRONMENT'] =='prod':
    # Oracle connection
    DATABASES = {
        'default': {
            'ENGINE': os.environ['ENGINE'],
            'NAME': os.environ['NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['PASSWORD'],
            # 'HOST':  os.environ['HOST'],
            # 'PORT': '1522',
        }
    }
elif os.environ['ENVIRONMENT'] =='test':
    # Oracle connection
    DATABASES = {
        'default': {
            'ENGINE': os.environ['ENGINE'],
            'NAME': os.environ['NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['PASSWORD'],
            # 'HOST':  os.environ['HOST'],
            # 'PORT': '1522',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE':  'django.db.backends.sqlite3',
            'NAME':  BASE_DIR/'db.sqlite3',
        }
    }





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
MEDIA_ROOT = os.path.join(BASE_DIR, 'grouping','media') # MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/grouping/media/'

# added for prod to launch the collect static command
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')



# added to prevent API errors
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# no limit to the number of parameters on get and post
DATA_UPLOAD_MAX_NUMBER_FIELDS = None

# email

EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']