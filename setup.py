#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Standard imports
#
import glob
import os
import sys
#
# setuptools' sdist command ignores MANIFEST.in
#
from distutils.command.sdist import sdist as DistutilsSdist
from setuptools import setup, find_packages
#
# DESI support code.
#
import desiutil.setup as ds
#
# Begin setup
#
setup_keywords = dict()
#
# THESE SETTINGS NEED TO BE CHANGED FOR EVERY PRODUCT.
#
setup_keywords['name'] = 'desidatamodel'
setup_keywords['description'] = 'DESI Data Model'
setup_keywords['author'] = 'DESI Collaboration'
setup_keywords['author_email'] = 'desi-data@desi.lbl.gov'
setup_keywords['license'] = 'BSD'
setup_keywords['url'] = 'https://github.com/desihub/desidatamodel'
#
# END OF SETTINGS THAT NEED TO BE CHANGED.
#
setup_keywords['version'] = ds.get_version(setup_keywords['name'])
#
# Use README.rst as long_description.
#
setup_keywords['long_description'] = ''
if os.path.exists('README.rst'):
    with open('README.rst') as readme:
        setup_keywords['long_description'] = readme.read()
#
# Set other keywords for the setup function.  These are automated, & should
# be left alone unless you are an expert.
#
# Treat everything in bin/ except *.rst as a script to be installed.
#
if os.path.isdir('bin'):
    setup_keywords['scripts'] = [fname for fname in glob.glob(os.path.join('bin', '*'))
        if not os.path.basename(fname).endswith('.rst')]
setup_keywords['provides'] = [setup_keywords['name']]
setup_keywords['python_requires'] = '>=3.5'
setup_keywords['zip_safe'] = False
setup_keywords['use_2to3'] = False
setup_keywords['packages'] = find_packages('py')
setup_keywords['package_dir'] = {'': 'py'}
setup_keywords['cmdclass'] = {'module_file': ds.DesiModule,
                              'version': ds.DesiVersion,
                              'test': ds.DesiTest,
                              'api': ds.DesiAPI,
                              'sdist': DistutilsSdist}
setup_keywords['test_suite']='{name}.test.{name}_test_suite'.format(**setup_keywords)
#
# Autogenerate command-line scripts.
#
# setup_keywords['entry_points'] = {'console_scripts': ['check_model = desidatamodel.check:main',
#                                                       'deep_scan_metadata = desidatamodel.scan:main',
#                                                       'generate_model = desidatamodel.stub:main',
#                                                       'update_bitmasks = desidatamodel.bitmasks:main',
#                                                       'update_column_descriptions = desidatamodel.update:main']}
#
# Add internal data directories.
#
setup_keywords['package_data'] = {'desidatamodel.test': ['t/*']}
#
# Run setup command.
#
setup(**setup_keywords)
