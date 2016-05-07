#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='funny_tool',
    version='0.1',
    description='The funny tools to download movies and comics',
    author='CCharlieLi',
    author_email='ccharlieli@live.com',
    url='https://github.com/CCharlieLi/funny_tool',
    download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
    keywords = ['download', 'bleach', 'dytt'], # arbitrary keywords
    license='MIT',
    packages=['funny_tool'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'funny_tool = funny_tool',
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)'
        ],
    )