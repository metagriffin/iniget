#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <metagriffin@uberdev.org>
# date: 2013/04/27
# copy: (C) CopyLoose 2013 UberDev <hardcore@uberdev.org>, No Rights Reserved.
#------------------------------------------------------------------------------

import os, sys, re, setuptools
from setuptools import setup, find_packages

# require python 2.7+
if sys.hexversion < 0x02070000:
  raise RuntimeError('This package requires python 2.7 or better')

heredir = os.path.abspath(os.path.dirname(__file__))
def read(*parts):
  try:    return open(os.path.join(heredir, *parts)).read()
  except: return ''

test_dependencies = [
  'nose                 >= 1.3.0',
  'coverage             >= 3.6',
  ]

dependencies = [
  'distribute           >= 0.6.24',
  'argparse             >= 1.2.1',
  'iniherit             >= 0.1.6',
  'six                  >= 1.4.1',
  ]

entrypoints = {
  'console_scripts': [
    'iniget             = iniget.cli:main',
    ],
  }

classifiers = [
  'Development Status :: 4 - Beta',
#  'Development Status :: 5 - Production/Stable',
  'Programming Language :: Python',
  'Operating System :: OS Independent',
  'Natural Language :: English',
  'Environment :: Console',
  'Topic :: Utilities',
  'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
  ]

setup(
  name                  = 'iniget',
  version               = '0.2.0',
  description           = 'A command-line tool to extract values from an iniherit-enabled "INI" file.',
  long_description      = read('README.rst'),
  classifiers           = classifiers,
  author                = 'metagriffin',
  author_email          = 'metagriffin@uberdev.org',
  url                   = 'http://github.com/metagriffin/iniget',
  keywords              = 'ini configuration value extract inherit',
  packages              = find_packages(),
  platforms             = ['any'],
  include_package_data  = True,
  zip_safe              = True,
  install_requires      = dependencies,
  tests_require         = test_dependencies,
  test_suite            = 'iniget',
  entry_points          = entrypoints,
  license               = 'GPLv3+',
  )

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
