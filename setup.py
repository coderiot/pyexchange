#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='pyexchange',
    version='0.1.0',
    license='GPL',
    description='Consistent API wrapper for cryptocurrency exchanges.',
    author='peterr',
    author_email='email',
    url='https://github.com/coderiot/pyexchange/',
    install_requires=['request'],
    packages=['pyexchange',
              'pyexchange.exchange'],
)
