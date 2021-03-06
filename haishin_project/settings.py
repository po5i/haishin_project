"""
Django settings for haishin project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+6-(+(+gzyga2y08&o5n%ksz#2crs#xv#r7#l1dml!k5%d%v)b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'ckeditor',
    'haishin',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'haishin_project.urls'

WSGI_APPLICATION = 'haishin_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if 'RDS_HOSTNAME' in os.environ:    # A W S

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

    #AWS S3 storage
    #https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
    AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'Cache-Control': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'delidelux-uploads'
    AWS_ACCESS_KEY_ID = 'AKIAITAAK2ZMRAEMLUOA'
    AWS_SECRET_ACCESS_KEY = '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'

    AWS_S3_CUSTOM_DOMAIN = 's3-us-west-2.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    MEDIAFILES_LOCATION = 'uploads'
    #MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN_UPLOADS , MEDIAFILES_LOCATION)
    #DEFAULT_FILE_STORAGE = 'arcademe.storage.MediaStorage'
 
    STRIPE_KEY = "sk_live_ZIigps1f2BFCCFgnXwN52MtM"
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    MEDIA_ROOT = os.path.join(BASE_DIR, 'static','uploads')
    MEDIA_URL = '/uploads/'

    STRIPE_KEY = "sk_test_wCp2BPssuA9Si5gint7uhKaj"



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')


# LOG 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# MAIL
"""
SERVER_EMAIL = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
"""

ADMINS = (('Carlos', 'carlos.po5i@gmail.com'),)
MANAGERS = ADMINS

DEFAULT_CHARSET = 'utf-8'



TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                                "django.core.context_processors.debug",
                                "django.core.context_processors.i18n",
                                "django.core.context_processors.media",
                                "django.core.context_processors.static",
                                "django.core.context_processors.tz",
                                "django.contrib.messages.context_processors.messages",
                                "django.core.context_processors.request",
)


# REST
REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
 
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.IsAuthenticated',  #funciona!
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# CORS 
CORS_ORIGIN_ALLOW_ALL = True

# Google Maps Application
GMAPS_API_CLIENT_KEY = "AIzaSyCC6zrIDWXAa2TtlyKaN7ohrRxC3vWp5Uo"

#Shippify.co
#SHIPPIFY_API_KEY = 'ihai7pnb0atnqba69psc3di'               #prod
#SHIPPIFY_API_SECRET = '3371aed4f73724343cacfba60357a644'   #prod
SHIPPIFY_API_KEY = 'igl0adxjv0rn6iea0vd3g14i'               #test
SHIPPIFY_API_SECRET = '174b807a225ee5becb125368a1cec119'    #test
SHIPPIFY_DEBUG = True

# Pusher
PUSHER_APP_ID = '156720'
PUSHER_KEY = 'ac5e3597a8e60e9f12ef'
PUSHER_SECRET = 'ff43af410cb81f418b79'

# BRAINTREE
import braintree
MERCHANT_ID = "77w5vghgk6tm7k7g"
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=MERCHANT_ID,
                                  public_key="g84m83v6fyqdjrn4",
                                  private_key="8d9d3711cad0813389503c956af768cd")
BRAINTREE_MERCHANTS = {
    "CL": "delideluxcl",
    "AR": "delideluxar"
}


#Email
EMAIL_API_KEY = 'key-1079b6a210ddead58af4a7b5d8bfc55b'
EMAIL_API_BASE_URL = 'https://api.mailgun.net/v3/sandboxb6963014532c4459bfb9e0555b07ef94.mailgun.org'
EMAIL_FROM = 'Mailgun Sandbox <postmaster@sandboxb6963014532c4459bfb9e0555b07ef94.mailgun.org>'
EMAIL_API_USER = 'jorlusal'
EMAIL_API_PASSWORD = 'delidelux01'

# CKEDITOR
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
