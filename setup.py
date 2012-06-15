#!/usr/bin/env python

from setuptools import setup 
import email_login

setup(
    name='django-email-login',
    version=email_login.__version__,
    author='Tino de Bruijn',
    author_email='tinodb@gmail.com',
    url='http://bitbucket.org/tino/django-email-login',
    description='A Django application that enables you to have your users use their email address instead of their username',
    long_description=open('README.txt').read(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='MIT License',
    packages=['email_login'],
    include_package_data=True,
    zip_safe=False,
)

