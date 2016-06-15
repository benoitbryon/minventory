#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python packaging."""
import os
import sys

from setuptools import setup


#: Absolute path to directory containing setup.py file.
here = os.path.abspath(os.path.dirname(__file__))
#: Boolean, ``True`` if environment is running Python version 2.
IS_PYTHON2 = sys.version_info[0] == 2


NAME = 'minventoryapi'
DESCRIPTION = 'Server-side API implementation for minventory.'
README = open(os.path.join(here, 'README.rst')).read()
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u'Benoît Bryon'
EMAIL = 'benoit@marmelune.net'
LICENSE = 'BSD'
URL = 'https://github.com/benoitbryon/minventoryapi'
CLASSIFIERS = [
    'Framework :: Django',
    'Framework :: Django :: 1.9',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
]
KEYWORDS = []
PACKAGES = [NAME]
REQUIREMENTS = [
    'Django',
    'django-confit>=0.6',
    'django-cors-headers',
    'django-debug-toolbar',
    'django-filter',
    'django-rest-swagger',
    'django-uuidfield',
    'djangorestframework',
    'docutils',
    'Markdown',
    'setuptools',
]
ENTRY_POINTS = {
    'console_scripts': ['minventoryapi = minventoryapi.manage:main']
}
SETUP_REQUIREMENTS = ['setuptools']
TEST_REQUIREMENTS = []
EXTRA_REQUIREMENTS = {
    'test': TEST_REQUIREMENTS,
}


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=README,
        classifiers=CLASSIFIERS,
        keywords=' '.join(KEYWORDS),
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        install_requires=REQUIREMENTS,
        entry_points=ENTRY_POINTS,
        tests_require=TEST_REQUIREMENTS,
        setup_requires=SETUP_REQUIREMENTS,
        extras_require=EXTRA_REQUIREMENTS,
    )
