#!/usr/bin/env python
from jquerypluginbp.boilerplate import BOILERPLATE
import os
from setuptools import setup, find_packages
import sys

extra_kwargs = {}
extra_kwargs['install_requires'] = ['pystache==0.5.4', 'lice==0.4']
if sys.version_info < (2, 7):
    extra_kwargs['install_requires'].append('argparse')

setup(name="jquerypluginbp",
    packages=['jquerypluginbp'],
    package_dir={'jquerypluginbp': 'jquerypluginbp'},
    package_data={'jquerypluginbp': [os.path.join('boilerplate', boilerplate) for boilerplate in BOILERPLATE]},
    version="0.1.0",
    description="Script to generate boilerplate for you jquery plugin",
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    url="",
    keywords= "jquery plugin script boilerplate",
    entry_points = {
        'console_scripts': [
            'jquerypluginbp = jquerypluginbp.main:main',
        ],
    },
    zip_safe = False,
    **extra_kwargs)
