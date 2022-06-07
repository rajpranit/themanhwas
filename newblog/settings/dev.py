from .base import *

SECRET_KEY = 'django-insecure-4m3^ojd1)qts!^e=vq4h-)6y5&s=(l0la-43av)z_%y5vwo4j-'


DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'

MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    'static/'
]

# STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_ROOT = BASE_DIR / 'media/'
