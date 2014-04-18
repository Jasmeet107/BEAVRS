from openmoc import *
import openmoc.log as log #stores data printed during simulation
import openmoc.plotter as plotter
import openmoc.materialize as materialize
import openmoc.process as process
import h5py
import numpy as np

import surfaces
#import materials

# Keys are Surface string names and values are OpenCSG Surfaces.
pincells = dict() #dictionary of pin cells


################################################################################
#############################  1.6% Enriched Fuel Pins #########################
################################################################################

pincells['16fuel'] = {} #dictionary of cells within this particular pin cell
pincells['16fuel']['fuelid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['16fuel']['fuel'] = CellBasic(universe=pincells['16fuel']['fuelid'], material='d1') #initializes inner fuel cell
pincells['16fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

#CLADDING
pincells['16fuel']['clad'] = CellBasic(universe=pincells['16fuel']['fuelid'], material='d2') #initializes cladding cell
pincells['16fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
pincells['16fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

#WATER
pincells['16fuel']['water'] = CellBasic(universe=pincells['16fuel']['fuelid'], material='d3') #initializes water cell
pincells['16fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
pincells['16fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of 3rd circle 

################################################################################
#############################  2.4% Enriched Fuel Pins #########################
################################################################################
pincells['24fuel'] = {} #dictionary of cells within this particular pin cell
pincells['24fuel']['24fuelid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['24fuel']['fuel'] = CellBasic(universe=pincells['24fuel']['fuelid'], material='d1') #initializes inner fuel cell
pincells['24fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

#CLADDING
pincells['24fuel']['clad'] = CellBasic(universe=pincells['24fuel']['fuelid'], material='d2') #initializes cladding cell
pincells['24fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
pincells['24fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

#WATER
pincells['24fuel']['water'] = CellBasic(universe=pincells['24fuel']['fuelid'], material='d3') #initializes water cell
pincells['24fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
pincells['24fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of 3rd circle 

"""

################################################################################
##########################  Guide Tube Pin Cell  ###############################
################################################################################

surfaces['GT Radius-1'] = Circle(x=0.0, y=0.0, radius=0.56134)
surfaces['GT Radius-2'] = Circle(x=0.0, y=0.0, radius=0.60198)


################################################################################
#######################  Instrument Tube Pin Cell  #############################
################################################################################

surfaces['IT Radius-1'] = Circle(x=0.0, y=0.0, radius=0.43688)
surfaces['IT Radius-2'] = Circle(x=0.0, y=0.0, radius=0.48387)


################################################################################
#######################  Burnable Absorber Pin Cell  ###########################
################################################################################

surfaces['BA Radius-1'] = Circle(x=0.0, y=0.0, radius=0.21400)
surfaces['BA Radius-2'] = Circle(x=0.0, y=0.0, radius=0.23051)
surfaces['BA Radius-3'] = Circle(x=0.0, y=0.0, radius=0.24130)
surfaces['BA Radius-4'] = Circle(x=0.0, y=0.0, radius=0.42672)
surfaces['BA Radius-5'] = Circle(x=0.0, y=0.0, radius=0.43688)
surfaces['BA Radius-6'] = Circle(x=0.0, y=0.0, radius=0.48387)
surfaces['BA Radius-7'] = Circle(x=0.0, y=0.0, radius=0.56134)
surfaces['BA Radius-8'] = Circle(x=0.0, y=0.0, radius=0.60198)



"""
