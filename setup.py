#!/usr/bin/env python
import os, sys
from setuptools import setup

if sys.argv[-1] == 'test':
    os.system('/usr/bin/env python3 manage.py test')
    sys.exit()

setup(
    name = 'bps',
    version = '1.0.5',
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
        # requirements are already specified in debian/control
    ],
)
