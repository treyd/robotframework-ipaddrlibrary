'''
Created on Jan 17, 2013

@author: Trey Duskin
'''

from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from IPAddrLibrary import __version__

setup(
      name = 'robotframework-ipaddrlibrary',
      version = __version__,
      description = "IP address and hostname manipulation library for Robot Framework",
      url = "http://github.com/tduskin/robotframework-ipaddrlibrary",
      packages = ['IPAddrLibrary'],
      package_dir = {'' : 'src'},
      author = "Trey Duskin",
      author_email = "trey@maldivica.com"
      )
