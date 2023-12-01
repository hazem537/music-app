"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#  fire base storage

FIREBASE_STORAGE_BUCKET = "music-app-84798.appspot.com"
FIREBASE_SERVICE_ACCOUNT_KEY = 'music-app-84798-firebase-adminsdk-thx4k-66896e648f.json'
FIREBASE_SERVICE_ACCOUNT_KEY_PATH =   BASE_DIR / FIREBASE_SERVICE_ACCOUNT_KEY
import firebase_admin
from firebase_admin import credentials
import base64
import json ,os

credentials_dict = {
    "type": "service_account",
    "project_id": "music-app-84798",
    "private_key_id": "66896e648f8fafcfaf5fc5b2566148ac1664a2c9",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDXaEyesxB03tLM\nwrwzuV+hDuyew7y5Qbjbxre4Zyj5GRb1G34CsF4peRHcTqlj/VmyUEzIV9Iv0Ky8\neDdDc9pV2vKS9lqnHSLvIRGwg7R5iYUoE8HchWCElIVW14IOiWmXfU+66jYDwQZl\nITKaz3EXmQbFFnV0/KfqafHl/85Uvw84PFVZ9euuW0cx7OGZ/h7bieW/Sa1AFcYQ\nrFYFpt0FH7RDQ147d7BErtRy5UqMLwWQ1v1Rw6S6gHspsjOU6sw+vV4r0nPw7b6M\n98s61SGeD//D/bwvmFXhoN24BTMqVktoF9KNHeN9i9ml9eT1oUH4ok6Kuy6vyF4b\nWz4o//qnAgMBAAECggEAOhnS2Nd5r9xORZadBuKQTbPl1Oj85Yc5omYWNfH1VkMT\nMyeoNHd33n3eeGrrO6IhaHxKSZuOgQErJmbSmSoNkSzOUx+J0huEybVEvTS5IDMc\nrHOvzZhYMUqSMJtOZDdiOM8/Cy6TRS3yWKK8sI8VdQT8k3p8UgK4E/1hluUJtUeY\niQbYrXjdYxeTPfr6DPu3OXBI0xQFCqVmzRXqRE45UNSVqeCW+hL3yYS0pJDxuVDm\nrNxBCeqaV12Ppb7qgxp1/NcR63yHYmjPTNqWWJM3HFGfy0OldChbxdy791u5hW7A\nJ0N5JsP3fkpqlOBWl6tXAw02GN4Yt0m9Nqmi6eRl6QKBgQD70bUp17FfH8zdyh2h\nW0wUbYcHz0/mXA3Ic+tBa2DGIcMYjmL3EwxCH4u/dk5ivnOa2cc5sSh+9baSYsG3\nGHtkTPVABZwRkvlWwBU9syBD/yvWc3f6RM3Wo0lwHeh7XKwz/a8+AU2bOgEXjArp\nvrWoWXDjepcxL6iAGKIoCIvCNQKBgQDa+9U33zhxrcBToYDJWPRz3yNRSDPvblQs\nrA0qD9jItobQ/nTYt4Sd20VuYXaXe2+PTOE/x6eruoIBaB3xHDAEPs+m5UhfdP4v\nYgmm0EDw6uWqd6z6pXfKciL5+cGkTuYRXKfrPzsGq7LU/wLmIOTe2uZEulEfWqNi\n6DGn8Hhk6wKBgC6dr4/DYg5d8KrOE5YfNIJDlE+ZzQyz1clZzB8cJZoH/fm5whBC\n8m37MP+Mgw48e2IbFopThU+bZOTMa1fdrFnw9SWY5D9MmeO5QzVcx4hO4GqejYNC\n4WfualXa84KCsU4elCZCT3+AyVr2jb6fkzlK9V7m/r4YOHUeGkaW7mhRAoGAcLfM\nKrRF044CP4oURo/5VGN5RG+L/CSoQ05UgGAj0DzT7GPuNVdRdgfWF1knuBWbeQGz\nuCbHEcgw/xRexSsjNCw4qsm+lRQderpWCX2Mz/W5PiPX8DSYEqbphg6fNDpAhpNR\nA/BKK8bZiHWzQk2QQX4fpSTaeO8oxtKKLM3Eyv0CgYBcS5aJD+v4ZLoYIEqIJ9AU\nkWOl71UNF/H3Ou6L2KCVqW4w55Q0tAfEcBc14xcJ1TBq+gqEO0EQkE4xayESt9jp\nzK95+0vW3i0a/QvQrMilEmnjyu+tH1t5q/VrQx1wNmAtzAU4hJFXb6FO7BB/gAmE\n8IEvshgUjSYwsbSXs0pF2g==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-thx4k@music-app-84798.iam.gserviceaccount.com",
    "client_id": "107602018648919657722",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-thx4k%40music-app-84798.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(credentials_dict)  
firebase_admin.initialize_app(cred, {'storageBucket': FIREBASE_STORAGE_BUCKET})

GS_BUCKET_NAME = FIREBASE_STORAGE_BUCKET
GS_DEFAULT_ACL = 'publicRead'  # Set the appropriate ACL for your needs
GS_FILE_OVERWRITE = False
GS_QUERYSTRING_AUTH = False

GS_CUSTOM_DOMAIN = f'{GS_BUCKET_NAME}.storage.googleapis.com'

# Use Google Cloud Storage as the default storage backend
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Set the media URL to the custom domain if available, otherwise use the default
MEDIA_URL = f'https://{GS_CUSTOM_DOMAIN}/' if GS_CUSTOM_DOMAIN else f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
# Use the Google Cloud Storage backend for Django storage
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-40^@@k4mymdr@k+k#$+kka-!$td2msjl)((%70p%^*r#_i#(nc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "music",
    "authentication",
    'widget_tweaks',
    'django_filters',
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default="postgres://default:0qe8HQNRiwJp@ep-aged-silence-54497879-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb")
}
LOGIN_URL = 'login'  # Set this to the URL of your login view
LOGOUT_URL = 'logout'  # Set this to the URL of your logout view
LOGIN_REDIRECT_URL = '/'  # Set this to the URL where users should be redirected after login
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
import os
STATIC_ROOT =os.path.join(BASE_DIR,"staticfiles_build","static")

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / "media"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
