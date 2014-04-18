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

#FUEL
pincells['uidfuel'] = universe_id() #sets universe ID for fuel
pincells['16fuel']['fuel'] = CellBasic(universe=pincells['uidfuel'], material='d1') #initializes inner fuel cell
pincells['16fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) 

#CLADDING
pincells['uidclad'] = universe_id() #sets universe ID for cladding
pincells['16fuel']['clad'] = CellBasic(universe=pincells['uidclad'], material='d2') #initializes cladding cell
pincells['16fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) 
pincells['16fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2'])

#WATER
pincells['uidwater'] = universe_id() #sets universe ID for water
pincells['16fuel']['water'] = CellBasic(universe=pincells['uidwater'], material='d3') #initializes water cell
pincells['16fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) 
pincells['16fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3'])

"""################################################################################
#############################  2.4% Enriched Fuel Pins #########################
################################################################################

#FUEL
pincells['24fuel'] = {} #dictionary of cells within this particular pin cell
pincells['24fuel']['fuel'] = CellBasic(universe=universe_id(), material='d1') #initializes inner fuel cell
pincells['24fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) 

#CLADDING
pincells['24fuel']['clad'] = CellBasic(universe=universe_id(), material='d2') #initializes cladding cell
pincells['24fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) 
pincells['24fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2'])

#WATER
pincells['24fuel']['water'] = CellBasic(universe=universe_id(), material='d3') #initializes water cell
pincells['24fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) 
pincells['24fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3'])"""

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




