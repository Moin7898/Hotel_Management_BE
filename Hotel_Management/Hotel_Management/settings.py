"""
Django settings for Hotel_Management project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from django.conf import settings
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vwa*6s)r8&f%vq+a&9@zyq8viulc#vb7zz!#n10f28@ph9k4%x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'daphne',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'drf_yasg',
    'rest_framework_simplejwt',
    'cloudinary_storage',
    'cloudinary',

    'core',
    'account',
    'table',
    'category',
    'item',
    'order',
    'bill'
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

ROOT_URLCONF = 'Hotel_Management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'Hotel_Management.wsgi.application'
ASGI_APPLICATION = 'Hotel_Management.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)]
        },
    },
}
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'account.user'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_files")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'utils.custom_exception_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "email",
    "USER_ID_CLAIM": "email_id"
}


# For add Jwt authentication in swagger
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "Auth Token eg [Bearer (JWT)]": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

# Email
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = "jaitun.flyontechsolution@gmail.com"
EMAIL_HOST_PASSWORD = "******"
EMAIL_USE_TLS = True
DEFAULT_SERVER_EMAIL = "jaitun.flyontechsolution@gmail.com"
DEFAULT_ACCOUNT_EMAIL = "jaitun.flyontechsolution@gmail.com"


# celery
CELERY_BROKER_URL = f"redis://127.0.0.1:6379"
CELERY_RESULT_BACKEND = 'db+sqlite:///db.sqlite3'


# cloudinary image storage
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drfdjango',
    'API_KEY': '****',
    'API_SECRET': '*****',
}

MEDIA_URL = 'hotel_management/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "console_handler": {
#             "class": "logging.StreamHandler",
#             "formatter": "simple",
#         },
#         "my_handler": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": f"{BASE_DIR}/logs/blogthedata.log",
#             "mode": "a",
#             "encoding": "utf-8",
#             "formatter": "simple",
#             "backupCount": 5,
#             "maxBytes": 1024 * 1024 * 5,  # 5 MB
#         },
#         "my_handler_detailed": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": f"{BASE_DIR}/logs/blogthedata_detailed.log",
#             "mode": "a",
#             "formatter": "verbose",
#             "backupCount": 5,
#             "maxBytes": 1024 * 1024 * 5,  # 5 MB
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console_handler", "my_handler_detailed"],
#             "level": "INFO",
#             "propagate": False,
#         },
#         "django.request": {
#             "handlers": ["my_handler"],
#             "level": "WARNING",
#             "propagate": False,
#         },
#     },
# }


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://1f73530a5e7742e1b6e468921058d5e1@o4504994316812288.ingest.sentry.io/4504994320416768",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
