#!/usr/bin/env python
import os, sys
from setuptools import setup

if sys.argv[-1] == 'test':
    os.system('/usr/bin/env python3 manage.py test')
    sys.exit()

setup(
    name = 'bps',
    version = '1.0.4',
    url = 'https://github.com/JaapJoris/bps',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    maintainer = 'Wessel Dankers',
    maintainer_email = 'wsl@fruit.je',
    license = 'AGPL',
    scripts = ['manage.py', 'bps_monitor/check_bps'],
    packages = ['bps', 'uvt_user', 'uvt_user.migrations'],
    include_package_data = True,
    install_requires = [
        'django >= 1.7.7, <= 1.9.4',
        'pillow >= 2.6.1, <= 3.1.1',
        'ldap3 == 1.4.0',
        'XlsxWriter == 0.9.6',
        'django-cleanup == 0.4.2',
        'autodidact >= 1.4.0',

        # This one is optional:
        'django-cas-client == 1.2.0',

        # These are for check_bps:
        'beautifulsoup4 >= 4.3.2',
        'requests >= 2.4.3',
        'termcolor >= 1.1.0',
    ],
)
