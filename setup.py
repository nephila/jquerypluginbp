#!/usr/bin/env python

from setuptools import setup, find_packages
import os
from jquerypluginbp.boilerplate import BOILERPLATE

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
    install_requires=[
        "pystache==0.5.4",
    ],
    entry_points = {
        'console_scripts': [
            'jquerypluginbp = jquerypluginbp.generate:main',
        ],
    },
    zip_safe = False)
