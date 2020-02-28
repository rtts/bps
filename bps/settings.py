import os, sys
import logging
import configparser
from django.core.exceptions import ImproperlyConfigured
from .utils import read, random_string

CONFIG_FILE = '/etc/bps/config.ini'
cfg = configparser.ConfigParser()
if os.path.isfile(CONFIG_FILE):
    try:
        cfg.read(CONFIG_FILE)
    except configparser.Error as e:
        raise ImproperlyConfigured("Error parsing %s: %s" % (CONFIG_FILE, e.message))

KEY_FILE = cfg.get('locations', 'secret_key', fallback='')
try:
    SECRET_KEY = read(KEY_FILE)
except IOError:
    logging.warning('Secret key not found. Using randomly generated key.')
    SECRET_KEY = random_string(50)

STATIC_ROOT = cfg.get('locations', 'static_dir', fallback='/srv/bps/static')
MEDIA_ROOT = cfg.get('locations', 'uploads_dir', fallback='/srv/bps/media')
CAS_SERVER_URL = cfg.get('misc', 'cas_server', fallback='')
CAS_RESPONSE_CALLBACKS = ['uvt_user.cas.callback']
ALLOWED_HOSTS = ['*']
DEBUG = cfg.get('misc', 'debug', fallback='true') in ['true', 'True', 'on', 'yes']
ROOT_URLCONF = 'bps.urls'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
WSGI_APPLICATION = 'bps.wsgi.application'
STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = False
USE_L10N = False
USE_TZ = True
CMS_PAGE_MODEL = 'pages.Page'
CMS_SECTION_MODEL = 'pages.Section'
if not DEBUG:
    SECURE_SSL_REDIRECT   = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE    = True

INSTALLED_APPS = [
    'autodidact',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polymorphic',
    'embed_video',
    'easy_thumbnails',
    'pandocfield',
    'uvt_user',
    'pages',
    'cms',
    'cas',
]

MIDDLEWARE = [
    'cms.middleware.SassMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'syslog': {
         'level': 'INFO',
         'class': 'logging.handlers.SysLogHandler',
         'facility': 'local7',
#         'address': '/dev/log',
       },
    },
    'loggers': {
        'django':{
            'handlers': ['syslog'],
            'level': 'INFO',
            'disabled': False
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + cfg.get('database', 'engine', fallback='postgresql'),
        'NAME': cfg.get('database', 'name', fallback='bps'),
        'HOST': cfg.get('database', 'hostname', fallback=None),
        'USER': cfg.get('database', 'username', fallback='bps'),
        'PASSWORD': cfg.get('database', 'password', fallback=None),
    }
}

if 'test' in sys.argv:
    MEDIA_ROOT = '/tmp/bps_unittest_files'
if DEBUG and 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
