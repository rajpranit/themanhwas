from pickle import FALSE
import django_on_heroku
from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = [
    'themanhwas.herokuapp.com',
]

# AWS S3 Settings

AWS_ACCESS_KEY_ID =  config('AWS_ACCESS_KEY_ID')    

AWS_SECRET_ACCESS_KEY =  config('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = F"{AWS_STORAGE_BUCKET_NAME}.s3.amazom.com "

AWS_DEFAULT_ACL = 'public-read'       

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400'
}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Access-Control-Allow-Origin':'*'
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = 'http://' + 'the-manhwas-bucket' + '.s3.us-west-2.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

#heroku logging

DEBUG_PROPOGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,
    'formatters':{
        'verbose':{
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple':{
            'format' : '%(levelname)s %(message)s'
        },
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class' : 'logging.StreamHandler',
        },
    },
    'loggers':{
        'MYAPP':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    }
}

# heroku setting

django_on_heroku.settings(locals() , staticfiles=False)
del DATABASES ['default'] ['OPTIONS'] ['sslmode']