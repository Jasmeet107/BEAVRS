from openmoc import *
import openmoc.log as log #stores data printed during simulation
import openmoc.plotter as plotter
import openmoc.materialize as materialize
import openmoc.process as process
import h5py
import numpy as np
import random as rand

import surfaces
#import materials

pincells = dict() #dictionary of pin cells


################################################################################
#############################  1.6% Enriched Fuel Pins #########################
################################################################################

pincells['16fuel'] = {} #dictionary of cells within this particular pin cell
pincells['16fuel']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['16fuel']['fuel'] = CellBasic(universe=pincells['16fuel']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes fuel cell
pincells['16fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1'].getId) #inside of innermost circle

#CLADDING
pincells['16fuel']['clad'] = CellBasic(universe=pincells['16fuel']['uid'], material=rand.randint(0,100)) #initializes cladding cell
pincells['16fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1'].getId) #outside of innermost (1st) circle
pincells['16fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2'].getId) #inside of 2nd circle

#WATER
pincells['16fuel']['water'] = CellBasic(universe=pincells['16fuel']['uid'], material=rand.randint(0,100)) #initializes water cell
pincells['16fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2'].getId) #outside of 2nd circle
pincells['16fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3'].getId) #inside of 3rd circle 

################################################################################
#############################  2.4% Enriched Fuel Pins #########################
################################################################################

pincells['24fuel'] = {} #dictionary of cells within this particular pin cell
pincells['24fuel']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['24fuel']['fuel'] = CellBasic(universe=pincells['24fuel']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes fuel cell
pincells['24fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1'].getId) #inside of innermost circle

#CLADDING
pincells['24fuel']['clad'] = CellBasic(universe=pincells['24fuel']['uid'], material=rand.randint(0,100)) #initializes cladding cell
pincells['24fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1'].getId) #outside of innermost (1st) circle
pincells['24fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2'].getId) #inside of 2nd circle

#WATER
pincells['24fuel']['water'] = CellBasic(universe=pincells['24fuel']['uid'], material=rand.randint(0,100)) #initializes water cell
pincells['24fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2'].getId) #outside of 2nd circle
pincells['24fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3'].getId) #inside of 3rd circle

################################################################################
#############################  3.1% Enriched Fuel Pins #########################
################################################################################

pincells['31fuel'] = {} #dictionary of cells within this particular pin cell
pincells['31fuel']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['31fuel']['fuel'] = CellBasic(universe=pincells['31fuel']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes fuel cell
pincells['31fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1'].getId) #inside of innermost circle

#CLADDING
pincells['31fuel']['clad'] = CellBasic(universe=pincells['31fuel']['uid'], material=rand.randint(0,100)) #initializes cladding cell
pincells['31fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1'].getId) #outside of innermost (1st) circle
pincells['31fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2'].getId) #inside of 2nd circle

#WATER
pincells['31fuel']['water'] = CellBasic(universe=pincells['31fuel']['uid'], material=rand.randint(0,100)) #initializes water cell
pincells['31fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2'].getId) #outside of 2nd circle
pincells['31fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3'].getId) #inside of 3rd circle


################################################################################
##########################  Guide Tube Pin Cells ###############################
################################################################################

pincells['guidetube'] = {} #dictionary of cells within this guide tube
pincells['guidetube']['uid'] = universe_id() #sets universe ID for pin cell

#WATER
pincells['guidetube']['water'] = CellBasic(universe=pincells['guidetube']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['guidetube']['water'].addSurface(halfspace=-1, surface=surfaces['GT Radius-1'].getId) #inside of innermost circle

#CLADDING
pincells['guidetube']['clad'] = CellBasic(universe=pincells['guidetube']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['guidetube']['clad'].addSurface(halfspace=+1, surface=surfaces['GT Radius-1'].getId) #outside of innermost circle
pincells['guidetube']['clad'].addSurface(halfspace=-1, surface=surfaces['GT Radius-2'].getId) #inside of 2nd circle


################################################################################
#######################  Instrument Tube Pin Cells  ############################
################################################################################
pincells['instube'] = {} #dictionary of cells within this guide tube
pincells['instube']['uid'] = universe_id() #sets universe ID for pin cell

#AIR
pincells['instube']['air'] = CellBasic(universe=pincells['instube']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['instube']['air'].addSurface(halfspace=-1, surface=surfaces['IT Radius-1'].getId) #inside of innermost circle

#CLADDING
pincells['instube']['clad'] = CellBasic(universe=pincells['instube']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['instube']['clad'].addSurface(halfspace=+1, surface=surfaces['IT Radius-1'].getId) #outside of innermost circle
pincells['instube']['clad'].addSurface(halfspace=-1, surface=surfaces['IT Radius-2'].getId) #inside of 2nd circle


################################################################################
#######################  Burnable Absorber Pin Cell  ###########################
################################################################################
pincells['bp'] = {} #dictionary of cells within this guide tube
pincells['bp']['uid'] = universe_id() #sets universe ID for pin cell

#AIR
pincells['bp']['air'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['air'].addSurface(halfspace=-1, surface=surfaces['BP Radius-1'].getId) #inside of innermost circle

#SS304
pincells['bp']['ss'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['ss'].addSurface(halfspace=+1, surface=surfaces['BP Radius-1'].getId) #outside of innermost circle
pincells['bp']['ss'].addSurface(halfspace=-1, surface=surfaces['BP Radius-2'].getId) #inside of 2nd circle

#AIR1
pincells['bp']['air1'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['air1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-2'].getId) #outside of 2nd circle
pincells['bp']['air1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-3'].getId) #inside of 3rd circle

#BOROSILICATE GLASS
pincells['bp']['bg'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['bg'].addSurface(halfspace=+1, surface=surfaces['BP Radius-3'].getId) #outside of 3rd circle
pincells['bp']['bg'].addSurface(halfspace=-1, surface=surfaces['BP Radius-4'].getId) #inside of 4th circle

#AIR2
pincells['bp']['air2'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['air2'].addSurface(halfspace=+1, surface=surfaces['BP Radius-4'].getId) #outside of 4th circle
pincells['bp']['air2'].addSurface(halfspace=-1, surface=surfaces['BP Radius-5'].getId) #inside of 5th circle

#SS3041
pincells['bp']['ss1'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['ss1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-5'].getId) #outside of 5th circle
pincells['bp']['ss1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-6'].getId) #inside of 6th circle

#WATER
pincells['bp']['water'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['water'].addSurface(halfspace=+1, surface=surfaces['BP Radius-6'].getId) #outside of 6th circle
pincells['bp']['water'].addSurface(halfspace=-1, surface=surfaces['BP Radius-7'].getId) #inside of 7th circle

#CLAD
pincells['bp']['clad'] = CellBasic(universe=pincells['bp']['uid'], material=rand.randint(0,100) #random integer for dummy material) #initializes water cell
pincells['bp']['clad'].addSurface(halfspace=+1, surface=surfaces['BP Radius-7'].getId) #outside of 7th circle
pincells['bp']['clad'].addSurface(halfspace=-1, surface=surfaces['BP Radius-8'].getId) #inside of 8th circle





