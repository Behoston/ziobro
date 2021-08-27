#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from os import path

from setuptools import find_packages
from setuptools import setup

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

test_requirements = []
with open(path.join(this_directory, 'test_requirements.txt')) as f:
    for line in f:
        require = line.split('#', 1)[0].strip()
        if require:
            test_requirements.append(require)

setup(
    name='ziobro',
    packages=find_packages(exclude=['tests']),
    version='0.00.0',
    url='https://github.com/Behoston/ziobro',
    license='THE BEER-WARE LICENSE',
    author='Behoston',
    author_email='mlegiecki@gmail.com',
    description='Pakiet pomocniczy dla programistów "Ziobro"',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['ziobro'],
    include_package_data=True,
    tests_require=test_requirements,
    setup_requires=['pytest-runner'] if needs_pytest else [],
    platforms='any',
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Polish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development',
    ],
)
