#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="jquery-plugin-boilerplate",
      py_modules=['generate'],
      version="0.1.0",
      description="Script to generate boilerplate for you jquery plugin",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="",
      keywords= "jquery plugin script boilerplate",
      entry_points = {
        'console_scripts': [
            'jqueryplugin = generate:main',
        ],
      },
      zip_safe = True)
