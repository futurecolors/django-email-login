#!/usr/bin/env python
 
from distutils.core import setup

setup(
    name='email_login',
    version='0.2',
    description='A Django application that enables you to have your users use their email address instead of their username',
    long_description=open('README.txt').read(),
    licences='MIT License, see LICENSE.txt',
    author='Tino de Bruijn',
    author_email='tinodb@gmail.com',
    url='http://bitbucket.org/tino/django-email-login',
    packages=['email_login'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)