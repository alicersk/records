#!/usr/bin/env python

from setuptools import setup

setup(
    name="records",
    version="0.0.1",
    packages=[],
    entry_points={
        'console_scripts': ['Records = Records.__main__:main']
        
    }
)