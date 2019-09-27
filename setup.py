#!/usr/bin/env python


import os
import sys

from setuptools import setup


setup(
    name='computervision',
    version='0.1.0',
    description='Computer Vision',
    keywords='computervision',
    url='https://github.com/cowboysmall/computervision',


    author='Jerry Kiely',
    author_email='jerry@cowboysmall.com',
    license='MIT',


    packages=['cv'],
    install_requires=[],


    zip_safe=False,


    classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],


    test_suite='nose.collector',
    tests_require=['nose'],
)
