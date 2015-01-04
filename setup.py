#!/usr/bin/env python

from setuptools import setup, find_packages
from boilerplate import BOILERPLATE
import os

setup(name="jquery-plugin-boilerplate",
    py_modules=['generate', 'boilerplate'],
    version="0.1.0",
    description="Script to generate boilerplate for you jquery plugin",
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    url="",
    keywords= "jquery plugin script boilerplate",
    data_files=[(os.path.join('bin', 'boilerplate', os.path.split(boilerfile)[0]),[os.path.join('boilerplate', boilerfile)]) for boilerfile in BOILERPLATE],
    install_requires=[
        "pystache==0.5.4",
    ],
    entry_points = {
        'console_scripts': [
            'jqueryplugin = generate:main',
        ],
    },
    zip_safe = True)
