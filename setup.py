#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='pyexchange',
    version='0.1.6',
    license='GPL',
    description='Consistent API wrapper for cryptocurrency exchanges.',
    author='peterr',
    author_email='coderiot@zoho.com',
    url='https://github.com/coderiot/pyexchange/',
    install_requires=['requests'],
    packages=['pyexchange',
              'pyexchange.exchange'],
)
