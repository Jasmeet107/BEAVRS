from openmoc import * 
from openmoc.compatible.casmo import *
import openmoc.plotter as plotter
import openmoc.log as log
import h5py
import numpy
import matplotlib.pyplot as plt
from beavrs2d import *
from beavrs2d.generatehdf5 import generate_some


assemblies = {'assembly1.6-0':'pwru160c00', 
							'assembly2.4-0':'pwru240c00', 
							'assembly2.4-12':'pwru240w12', 
							'assembly2.4-16':'pwru240w16', 
							'assembly3.1-0':'pwru310c00', 
							'assembly3.1-6b':'pwru310w06', 
							'assembly3.1-6l':'pwru310w06', 
							'assembly3.1-6r':'pwru310w06', 
							'assembly3.1-6t':'pwru310w06', 
							'assembly3.1-12':'pwru310w12', 
							'assembly3.1-15b':'pwru310w15', 
							'assembly3.1-15l':'pwru310w15', 
							'assembly3.1-15r':'pwru310w15', 
							'assembly3.1-15t':'pwru310w15', 
							'assembly3.1-16':'pwru310w16',
							'assembly3.1-20':'pwru310w20'}
							
							

for assembly in assemblies: 
	direc = ('studies/' + assembly + '/casmo-reference/')
	generate_some(assemblies[assembly], '8-group/', direc)
	
	