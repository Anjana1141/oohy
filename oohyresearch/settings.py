import os
from pathlib import Path
from env import AWS_ACCESS_KEY_ID
from env import AWS_SECRET_ACCESS_KEY
from env import AWS_STORAGE_BUCKET_NAME
from env import AWS_S3_REGION_NAME
from env import AWS_S3_SIGNATURE_NAME
from env import HOST
from env import NAME


# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'laptop-1dneaevu']

# Secret key
SECRET_KEY = "%v)q%$-o3qs3r!i6&kf3e1rh9tuf2#m-7q-j2!#nx@9&wu&^7+"

# Debug mode
DEBUG = True

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'datacollection', 
    'rest_framework',  
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = "oohyresearch.urls"

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI application
WSGI_APPLICATION = "oohyresearch.wsgi.application"

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'name': NAME,
        'COLLECTION':'collection',
        'CLIENT': {
            'host': HOST,
        },
    }
}


# AWS default
aws_access_key_id = AWS_ACCESS_KEY_ID
aws_secret_access_key = AWS_SECRET_ACCESS_KEY
aws_storage_bucket_name = AWS_STORAGE_BUCKET_NAME
aws_s3_region_name =  AWS_S3_REGION_NAME
aws_s3_signature_name = AWS_S3_SIGNATURE_NAME
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True

# Static and media file storage configurations
# STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % aws_storage_bucket_name

# Password validators
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# settings.p

STATIC_URL = '/static/'

# Static files (CSS, JavaScript, Images)


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
