from openmoc import CellBasic, universe_id
from surfaces import surfaces
from materials import materials
from openmoc import *

pincells = {} #dictionary of pin cells

pincells['2'] = {}
pincells['2']['pwru160c00'] = {} #dictionary of cells within this particular pin cell
pincells['2']['pwru160c00']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['2']['pwru160c00']['fuel'] = CellBasic(universe=pincells[group]['pwru160c00']['uid'], material= materials['2']['pwru160c00']['fuel'].getId()
pincells['2']['pwru160c00']['fuel'].addSurface(halfspace=-1, surface=Circle(x=0.0, y=0.0, radius=0.39218))
