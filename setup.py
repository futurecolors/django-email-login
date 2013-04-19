#!/usr/bin/env python

from setuptools import setup
import email_login

setup(
    name='django-email-login-fc',
    version=email_login.__version__,
    description='A Django application that enables you to have your users use their email address instead of their username',
    long_description=open('README.rst').read(),
    author='Ilya Baryshev',
    author_email='baryshev@futurecolors.ru',
    url='https://github.com/futurecolors/django-email-login',
    tests_require=(
        'django-setuptest',
    ),
    test_suite='setuptest.setuptest.SetupTestSuite',
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
    ],
    license='MIT License',
    include_package_data=True,
)
