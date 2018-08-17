#!/usr/bin/env python
"""
Refactored by Ulrich Eck <ueck@net-labs.de> August 2018

Copyright (c) 2015, Jairus Martin.
Distributed under the terms of the MIT License.
The full license is in the file COPYING.txt, distributed with this software.
Created on Mar 2, 2016
"""
from setuptools import setup, find_packages

setup(
    name='enaml_data',
    version='0.1',
    description='Tree and List Widgets Widgets for Enaml',
    long_description=open('README.md').read(),
    author='Ulrich Eck',
    author_email='ueck@net-labs.de',
    url='https://github.com/ulricheck/enaml_data',
    download_url='https://github.com/ulricheck/enaml_data/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['enaml', 'atom'],
    zip_safe=False,
    keywords=['enaml', 'qt', 'tree', 'table', 'widgets'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',        
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
