import os, sys
import logging
import configparser
from django.core.exceptions import ImproperlyConfigured
from .utils import read

HUMAN_FRIENDLY_CHARS = '234679ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
def random_string(length):
    return ''.join(random.choice(HUMAN_FRIENDLY_CHARS) for x in range(length))

if os.path.isfile('/etc/bps/config.ini'):
    CONFIG_FILE = '/etc/bps/config.ini'
elif os.path.isfile('bps/config.ini'):
    CONFIG_FILE = 'bps/config.ini'
else:
    raise ImproperlyConfigured('Could not locate the configuration file {/etc/,}bps/config.ini')

try:
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE)
    static_dir    = cfg.get('locations', 'static_dir')
    uploads_dir   = cfg.get('locations', 'uploads_dir')
    secret_key    = cfg.get('locations', 'secret_key')
    db_engine     = cfg.get('database', 'engine')
    db_name       = cfg.get('database', 'name')
    db_host       = cfg.get('database', 'hostname')
    db_user       = cfg.get('database', 'username')
    db_pass       = cfg.get('database', 'password')
    cas_server    = cfg.get('misc', 'cas_server', fallback='')
    allowed_hosts = cfg.get('misc', 'allowed_hosts')
    https_only    = cfg.get('misc', 'https_only') in ['true', 'True', 'on', 'yes']
    debug         = cfg.get('misc', 'debug') in ['true', 'True', 'on', 'yes']
except configparser.Error as e:
    raise ImproperlyConfigured("Error parsing %s: %s" % (CONFIG_FILE, e.message))

try:
    SECRET_KEY = read(secret_key)
except IOError:
    if debug or 'test' in sys.argv:
        logging.warning('Secret key not found. Using randomly generated key.')
        SECRET_KEY = random_string(50)
    else:
        raise ImproperlyConfigured('Could not read secret key file specified in config file: "{}"'.format(secret_key))

STATIC_ROOT = static_dir
MEDIA_ROOT = uploads_dir
CAS_SERVER_URL = cas_server
CAS_RESPONSE_CALLBACKS = ['uvt_user.cas.callback']
ALLOWED_HOSTS = [e.strip() for e in allowed_hosts.split(',')]
DEBUG = debug
ROOT_URLCONF = 'bps.urls'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
WSGI_APPLICATION = 'bps.wsgi.application'
PACKAGE_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = [os.path.join(PACKAGE_DIR, 'templates')]
STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N = False
USE_L10N = False
USE_TZ = True
if https_only and not DEBUG:
    SECURE_SSL_REDIRECT   = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE    = True

STATICFILES_DIRS = [
    os.path.join(PACKAGE_DIR, 'static'),
    '/usr/share/javascript',
]


INSTALLED_APPS = [
    'autodidact',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pandocfield',
    'uvt_user',
    'cas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'cas.middleware.CASMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': TEMPLATE_DIRS,
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
        'ENGINE': 'django.db.backends.' + db_engine,
        'NAME': db_name,
        'HOST': db_host,
        'USER': db_user,
        'PASSWORD': db_pass,
    }
}

if 'test' in sys.argv:
    MEDIA_ROOT = '/tmp/bps_unittest_files'
if DEBUG and 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
