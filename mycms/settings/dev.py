# -*- coding: utf-8 -*-
from .defaults import *
import logging

DEBUG = True

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_mycms_cache',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# will output to your console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)

# 调试模板
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

THUMBNAIL_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEFAULT_FROM_EMAIL = ''
# EMAIL_HOST = ''
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = '8'

# ACCOUNT_ACTIVATION_DAYS = 3

# 分类文章需要登录才能查看，在这里设置分类
LOGIN_REQUIRED_CATEGORY = ['tech']
