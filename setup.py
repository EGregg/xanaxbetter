#!/usr/bin/env python
'''
Installer script for whatbetter.
'''

from setuptools import setup

import re
VERSIONFILE="_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name = "xanaxbetter",
    description = "Automatically transcode and upload FLACs on Xanax.Rip.",
    author = 'Zach Denton',
    author_email = 'zacharydenton@gmail.com',
    version = verstr,
    url = 'http://github.com/zacharydenton/whatbetter',
    py_modules = [
        '_version',
        'tagging',
        'transcode',
        'xanaxapi'
    ],
    scripts = ['xanaxbetter'],
    install_requires = [
        'mutagen',
        'mechanize',
        'requests'
    ]
)
