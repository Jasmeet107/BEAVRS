__author__ = 'Sam Shaner'
__email__ = 'samuelshaner@gmail.com'

from distutils.core import setup

setup(name='beavrs2d',
      version='0.1',
      description='beavrs 2d',
      author='Sam Shaner',
      author_email='samuelshaner@gmail.com',
      package_data={'beavrs2d': ['Cross-Section-Output/*/*.txt']},
      packages=['beavrs2d'],
      )
