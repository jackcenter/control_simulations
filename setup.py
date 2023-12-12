#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tractor_trailer',
      version='0.1',
      description='Tractor trailer modeling tools',
      author='Jack Center',
      author_email='jack.d.center@gmail.com',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=[
        'matplotlib',
        'numpy',
        'scipy'
      ]
     )