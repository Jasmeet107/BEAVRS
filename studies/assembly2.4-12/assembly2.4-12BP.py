from beavrs2d import *
from beavrs2d.lattices import pin_pitch
from openmoc import *
import openmoc.log as log
import openmoc.plotter as plotter
from openmoc.options import Options
import openmoc.process as process
from openmoc.compatible.casmo import *
from beavrs2d.tester import *

group_types = ['2-group/','8-group/']
assembly_name = 'pwru240w12' 

###############################################################################
#######################   Main Simulation Parameters   ########################
###############################################################################

options = Options()

num_threads = options.getNumThreads()
track_spacing = options.getTrackSpacing()
num_azim = options.getNumAzimAngles()
tolerance = options.getTolerance()
max_iters = options.getMaxIterations()

log.set_log_level('NORMAL')

log.py_printf('TITLE', 'Simulating the BEAVRS 2.4 pct enriched 12 BP assembly...')
  
group = '8'
assembly = CellFill(universe=0, universe_fill= lattices[group]['2.4-12BP'].getId())

###############################################################################
###########################   Creating Surfaces   #############################
###############################################################################

log.py_printf('NORMAL', 'Creating surfaces...')

#create surfaces
left = openmoc.XPlane(x=-pin_pitch*17/2.0)
right = openmoc.XPlane(x=pin_pitch*17/2.0)
bottom = openmoc.YPlane(y=-pin_pitch*17/2.0)
top = openmoc.YPlane(y=pin_pitch*17/2.0)

#sets boundary condition to be reflective
left.setBoundaryType(REFLECTIVE)
right.setBoundaryType(REFLECTIVE)
bottom.setBoundaryType(REFLECTIVE)
top.setBoundaryType(REFLECTIVE)

#add surfaces to bound cell
assembly.addSurface(halfspace=+1, surface=left)
assembly.addSurface(halfspace=-1, surface=right)
assembly.addSurface(halfspace=+1, surface=bottom)
assembly.addSurface(halfspace=-1, surface=top)

###############################################################################
##########################     Creating Cmfd mesh    ##########################
###############################################################################

log.py_printf('NORMAL', 'Creating Cmfd mesh...')

cmfd = Cmfd()
cmfd.setLatticeStructure(17,17)

###############################################################################
##########################   Creating the Geometry   ##########################
###############################################################################

geometry = Geometry()
geometry.setCmfd(cmfd)

#add materials
materialtypes = ['fuel', 'cladding', 'helium', 'water', 'ss304', 'bp']
for material in materialtypes:
  geometry.addMaterial(materials[group]['pwru240w12'][material])

#add surfaces
geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(bottom)
geometry.addSurface(top)

for surface in surfaces:
  geometry.addSurface(surfaces[surface])

#add cells
geometry.addCell(pincells[group]['pwru240w12']['fuel'])
geometry.addCell(pincells[group]['pwru240w12']['cladding'])
geometry.addCell(pincells[group]['pwru240w12']['water'])
geometry.addCell(pincells[group]['pwru240w12']['helium'])
geometry.addCell(pincells[group]['pwru240w12']['guidetube']['water1'])
geometry.addCell(pincells[group]['pwru240w12']['guidetube']['water2'])
geometry.addCell(pincells[group]['pwru240w12']['guidetube']['cladding'])
geometry.addCell(pincells[group]['pwru240w12']['instube']['cladding1'])
geometry.addCell(pincells[group]['pwru240w12']['instube']['helium'])
geometry.addCell(pincells[group]['pwru240w12']['instube']['cladding2'])
geometry.addCell(pincells[group]['pwru240w12']['instube']['water1'])
geometry.addCell(pincells[group]['pwru240w12']['instube']['water2'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['helium'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['ss'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['helium1'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['bg'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['helium2'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['ss1'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['water'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['cladding'])
geometry.addCell(pincells[group]['pwru240w12']['bp']['water1'])
geometry.addCell(assembly)

#add pincell lattice
geometry.addLattice(lattices[group]['2.4-12BP'])

#initialize flat source regions
geometry.initializeFlatSourceRegions()

num_azims = [i for i in range(4, 132, 4)]

for num_azim in num_azims: 

	###############################################################################
	########################   Creating the TrackGenerator   ######################
	###############################################################################

	log.py_printf('NORMAL', 'Initializing the track generator...')
	track_generator = TrackGenerator(geometry, num_azim, track_spacing)
	track_generator.generateTracks()

	###############################################################################
	###########################   Running a Simulation   ##########################
	###############################################################################

	solver = CPUSolver(geometry, track_generator)
	solver.setSourceConvergenceThreshold(tolerance)
	solver.setNumThreads(num_threads)
	solver.convergeSource(max_iters)
	solver.printTimerReport()
	
	if num_azim == num_azims[0]:
		process.store_simulation_state(solver, fission_rates=True, use_hdf5=True, append=False)
	else: 
		process.store_simulation_state(solver, fission_rates=True, use_hdf5=True, append=True)