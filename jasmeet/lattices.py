from openmoc import Lattice, universe_id
import openmoc.plotter as plotter
from pincells import pincells

lattices = dict() #creates dictionary of lattices



################################################################################
#############################  1.6% Enriched Fuel Pins #########################
################################################################################
f16 = pincells['16fuel']['uid']
gTi = pincells['guidetube']['uid']
iTi = pincells['instube']['uid']

lattices['16'] = Lattice(id=universe_id(), width_x = 1.25984, width_y = 1.25984)
lattices['16'].setLatticeCells([
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, f16, f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16, f16, f16, f16],
    [f16, f16, f16, gTi, f16, f16, f16, f16, f16, f16, f16, f16, f16, gTi, f16, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, gTi, f16, f16, gTi, f16, f16, iTi, f16, f16, gTi, f16, f16, gTi, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, f16, gTi, f16, f16, f16, f16, f16, f16, f16, f16, f16, gTi, f16, f16, f16],
    [f16, f16, f16, f16, f16, gTi, f16, f16, gTi, f16, f16, gTi, f16, f16, f16, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
    [f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16, f16],
])

lattices['16'].printString()
