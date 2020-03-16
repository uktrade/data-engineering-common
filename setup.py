#!/usr/bin/env python

from distutils.core import setup

setup(
    name='data-engineering-common',
    version='1.0',
    package_dir={'': 'src'},
    install_requires=[
        'python-dotenv>=0.12.0'
    ]
)
