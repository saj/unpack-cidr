#!/usr/bin/env python

# pylint: disable=missing-docstring

from setuptools import setup

import _about


setup(
    name=_about.NAME,
    version=_about.VERSION,
    description=_about.DESCRIPTION,

    author=_about.AUTHOR,
    author_email=_about.EMAIL,

    py_modules=["_about", "_version", "unpack_cidr"],

    entry_points={
        "console_scripts": [
            "unpack-cidr = unpack_cidr:main",
        ],
    },

    install_requires=[
        "ipaddress",
        "six",
        "sortedcontainers",
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
    ],
)
