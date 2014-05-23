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
VERSION = "3.11.0"

from setuptools import setup
import sys

if sys.version_info < (2, 6):
    print("This version of ZODB requires Python 2.6 or higher")
    sys.exit(0)

classifiers = """\
Intended Audience :: Developers
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: Implementation :: CPython
Topic :: Database
Operating System :: Microsoft :: Windows
Operating System :: Unix
Framework :: ZODB
"""

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
)

setup(
    name="ZODB3",
    version=VERSION,
    maintainer="Zope Foundation and Contributors",
    maintainer_email="zodb-dev@zope.org",
    license="ZPL 2.1",
    platforms=["any"],
    description=long_description.split('\n', 2)[1],
    long_description=long_description,
    classifiers=filter(None, classifiers.split("\n")),
    install_requires=[
        'ZEO >=4.0.0dev',
        'ZODB >=4.0.0dev',
        'persistent >=4.0.0dev',
        'BTrees >=4.0.0dev',
        'transaction'],
    zip_safe=False,
    extras_require=dict(
        test=[
            'ZEO [test]',
            'ZODB [test]',
            'BTrees [test]',
            'persistent [test]',
        ],
    )
)
