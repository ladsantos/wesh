#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="wesh",
    version="0.1a",
    author="Leonardo dos Santos",
    author_email="ldsantos@stsci.edu",
    packages=["wesh"],
    url="https://github.com/ladsantos/wesh",
    license="MIT",
    description="Weaver of Echelle Spectra from Hubble",
    install_requires=[line.strip() for line in
                      open('requirements.txt', 'r').readlines()],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
