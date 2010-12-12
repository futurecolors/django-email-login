#!/usr/bin/env python
 
from distutils.core import setup

packages = ['email_login']

setup(
    name='email_login',
    version='0.1',
    description='A Django application that enables you to have your users use their email address instead of their username',
    author='Tino de Bruijn',
    author_email='tinodb@gmail.com',
    packages=packages,
    zip_safe=False,
)