# -*- coding: utf-8 -*-
#
# © 2014, 2015 Ian Eure.
# Author: Ian Eure <ian.eure@gmail.com>
#
from setuptools import setup, find_packages


setup(name="tubular",
      version="2.0.0",
      packages=find_packages(),
      install_requires=['pystache==0.5.4'],
      entry_points={
          'console_scripts': ['mktubes = tubular.make_tubes:main',
                              'mkmonitors = tubular.make_monitors:main',
                              'mkmonitorid = tubular.make_monitorid:main']},
      package_data={'tubular': 'data/*.json'},
      include_package_data=True,
      tests_require=['nose'],
      test_suite="nose.collector")
