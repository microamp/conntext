#!/usr/bin/env python

import os
import sys

import conntext

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

short = "Context managers for database connectivity"

setup(name="conntext",
      version=conntext.__version__,
      description=short,
      author="James Sangho Nah",
      author_email="sangho.nah@gmail.com",
      url="https://github.com/microamp/conntext",
      packages=["conntext"],
      package_data={"": ["LICENSE", "README.md"]},
      include_package_data=True,
      install_requires=[],
      license=open("LICENSE").read(),
      zip_safe=False,
      classifiers=("Development Status :: 2 - Pre-Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "License :: OSI Approved :: Apache Software License",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.1",
                   "Programming Language :: Python :: 3.2",
                   "Programming Language :: Python :: 3.3"))
