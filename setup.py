
__author__ = 'Jasmeet Arora'
__email__ = 'jasmeet@mit.edu'


from setuptools import setup
import os

file_name_list2 = os.listdir('beavrs/Cross-Section-Output/2-group/')
file_name_list8 = os.listdir('beavrs/Cross-Section-Output/8-group/')

list_2 = []
list_8 = []

for filename in file_name_list2: 
  list_2.append("beavrs/Cross-Section-Output/2-group/"+filename)

for filename in file_name_list8:
	list_8.append("beavrs/Cross-Section-Output/8-group/"+filename)
     
setup(name='beavrs',
      version='0.1',
      description='beavrs',
      author='Jasmeet Arora',
      author_email='jasmeet@mit.edu',
      packages=['beavrs'],
      include_package_data = True,
      install_requires = [],
      package_data = {'beavrs': ['Cross-Section-Output/2-group/*.txt', 'Cross-Section-Output/8-group/*.txt']}
     )
     
     
     
     
"""setup(name='beavrs',
      version='0.1',
      description='beavrs',
      author='Jasmeet Arora',
      author_email='jasmeet@mit.edu',
      packages=['beavrs'],
      data_files = [('beavrs/casmo-data/2-group', list_2), ('beavrs/casmo-data/8-group', list_8)]
      
     )"""
     
     