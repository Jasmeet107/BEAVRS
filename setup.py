__author__ = 'Jasmeet Arora'
__email__ = 'jasmeet@mit.edu'

from distutils.core import setup

setup(name='beavrs2d',
      version='0.1',
      description='beavrs 2d',
      author='Jasmeet Arora',
      author_email='jasmeet@mit.edu',
      package_data={'beavrs2d': ['Cross-Section-Output/*/*.txt']},
      packages=['beavrs2d'],
      )
