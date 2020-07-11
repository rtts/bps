#!/usr/bin/env python3
import os, sys, bps
from setuptools import setup, find_packages

if sys.argv[-1] == 'test':
    os.system('/usr/bin/env python3 manage.py test')
    sys.exit()

setup(
    name = 'bps',
    version = bps.__version__,
    url = 'https://github.com/rtts/bps',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    maintainer = 'Wessel Dankers',
    maintainer_email = 'wsl@fruit.je',
    license = 'AGPL',
    scripts = ['manage.py', 'monitor/check_bps'],
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'bleach==3.1.5',
        'Django==3.0.8',
        'django-cas-client==1.5.3',
        'django-embed-video==1.3.3',
        'django-extensions==3.0.2',
        'django-simplecms @ git+https://github.com/rtts/django-simplecms',
        'easy-thumbnails==2.7',
        'ldap3==2.7',
        'libsass==0.20.0',
        'Markdown==3.2.2',
        'Pillow==7.2.0',
        'psycopg2==2.8.5',
    ],
)
