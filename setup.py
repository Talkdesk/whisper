#!/usr/bin/env python

import os
import platform
from glob import glob

if os.environ.get('USE_SETUPTOOLS'):
  from setuptools import setup
  setup_kwargs = dict(zip_safe=0)
else:
  from distutils.core import setup
  setup_kwargs = dict()


setup(
  name='whisper',
  version='0.9.12',
  url='http://graphite-project.github.com/',
  author='Chris Davis',
  author_email='chrismd@gmail.com',
  license='Apache Software License 2.0',
  description='Fixed size round-robin style database',
  py_modules=['whisper'],
  scripts=glob('bin/*'),
)
