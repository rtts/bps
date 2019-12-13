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
        # requirements are already specified in debian/control
    ],
)
