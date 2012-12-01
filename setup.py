##############################################################################
#
# Copyright (c) 2002, 2003 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
VERSION = "3.11.0a1"

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup
import os
import sys

if sys.version_info < (2, 6):
    print "This version of ZODB requires Python 2.6 or higher"
    sys.exit(0)

classifiers = """\
Intended Audience :: Developers
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Microsoft :: Windows
Operating System :: Unix
Framework :: ZODB
"""

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    )

tests_require = ['ZEO [test]', 'ZODB [test]', 'persistent [test]'],

setup(name="ZODB3",
      version=VERSION,
      maintainer="Zope Foundation and Contributors",
      maintainer_email="zodb-dev@zope.org",
      license = "ZPL 2.1",
      platforms = ["any"],
      description = long_description.split('\n', 2)[1],
      long_description = long_description,
      classifiers = filter(None, classifiers.split("\n")),
      install_requires = [
          'ZEO >=4.0.0dev, <4.1dev',
          'ZODB >=4.0.0dev, <4.1dev',
          'persistent >=4.0.0dev, <4.1dev',
          'BTrees >=4.0.0dev, <4.1dev',
          'transaction'],
      zip_safe = False,
      )
