#!/usr/bin/env python

from distutils.core import setup

setup(name='logstash',
      version='0.1dev',
      description='Python library for Logstash',
      author='Matt McClean',
      author_email='matt.mcclean@gmail.com',
      packages=['logstash', 'logstash.test'],
      license='LICENSE.txt',
      long_description=open('README.txt').read(),
     )
