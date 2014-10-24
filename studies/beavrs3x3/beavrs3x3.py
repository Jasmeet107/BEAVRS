from beavrs2d import *
from beavrs2d.lattices import pin_pitch
from openmoc import *
import openmoc.log as log
import openmoc.plotter as plotter
from openmoc.options import Options

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

log.py_printf('TITLE', 'Simulating a BEAVRS 3x3 small core...')

group = '8'

###############################################################################
###########################   Creating Lattices   #############################
###############################################################################

log.py_printf('NORMAL', 'Creating lattices...')

assembly16 = CellFill(universe=universe_id(), universe_fill= lattices[group]['1.6-0BP'].getId())
assembly24 = CellFill(universe=universe_id(), universe_fill= lattices[group]['2.4-16BP'].getId())
id16 = assembly16.getUniverseId()
id24 = assembly24.getUniverseId()

smallcore = Lattice(universe_id(), pin_pitch*17, pin_pitch*17)
smallcore.setLatticeCells([[id16, id24, id16],
                          [id24, id16, id24],
                          [id16, id24, id16]])

###############################################################################
###########################   Creating Surfaces   #############################
###############################################################################

log.py_printf('NORMAL', 'Creating surfaces...')

#create surfaces
left = openmoc.XPlane(x=-pin_pitch*17*3/2.0)
right = openmoc.XPlane(x=pin_pitch*17*3/2.0)
bottom = openmoc.YPlane(y=-pin_pitch*17*3/2.0)
top = openmoc.YPlane(y=pin_pitch*17*3/2.0)

#sets boundary condition to be reflective
left.setBoundaryType(REFLECTIVE)
right.setBoundaryType(REFLECTIVE)
bottom.setBoundaryType(REFLECTIVE)
top.setBoundaryType(REFLECTIVE)

#add surfaces to bound cell
core = CellFill(universe=0, universe_fill = smallcore.getId())
core.addSurface(halfspace=+1, surface=left)
core.addSurface(halfspace=-1, surface=right)
core.addSurface(halfspace=+1, surface=bottom)
core.addSurface(halfspace=-1, surface=top)

###############################################################################
##########################     Creating Cmfd mesh    ##########################
###############################################################################

log.py_printf('NORMAL', 'Creating Cmfd mesh...')

cmfd = Cmfd()
cmfd.setLatticeStructure(51,51)

###############################################################################
##########################   Creating the Geometry   ##########################
###############################################################################

log.py_printf('NORMAL', 'Creating geometry...')

geometry = Geometry(cmfd)

names = ['pwru160c00','pwru240w16']
bps = ['pwru240w12', 'pwru240w16', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

# add materials
for name in names:
  if name in bps:
    materialtypes = ['fuel', 'cladding', 'helium', 'water', 'ss304', 'bp']
  else:
    materialtypes = ['fuel', 'cladding', 'helium', 'water']
  for material in materialtypes:
    #add materials
    geometry.addMaterial(materials[group][name][material])

# add surfaces 
for surface in surfaces:
  geometry.addSurface(surfaces[surface])

geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(top)
geometry.addSurface(bottom)

# add cells
for name in names:

  # fuel pins
  geometry.addCell(pincells[group][name]['fuel'])
  geometry.addCell(pincells[group][name]['cladding'])
  geometry.addCell(pincells[group][name]['water'])
  geometry.addCell(pincells[group][name]['helium'])

  # guidetube
  geometry.addCell(pincells[group][name]['guidetube']['water1'])
  geometry.addCell(pincells[group][name]['guidetube']['water2'])
  geometry.addCell(pincells[group][name]['guidetube']['cladding'])
  
  # instrument tube
  geometry.addCell(pincells[group][name]['instube']['helium'])
  geometry.addCell(pincells[group][name]['instube']['cladding1'])
  geometry.addCell(pincells[group][name]['instube']['cladding2'])
  geometry.addCell(pincells[group][name]['instube']['water1'])
  geometry.addCell(pincells[group][name]['instube']['water2'])
    
  # burnable poison
  if name in bps:
    geometry.addCell(pincells[group][name]['bp']['helium'])
    geometry.addCell(pincells[group][name]['bp']['ss'])
    geometry.addCell(pincells[group][name]['bp']['helium1'])
    geometry.addCell(pincells[group][name]['bp']['bg'])
    geometry.addCell(pincells[group][name]['bp']['helium2'])
    geometry.addCell(pincells[group][name]['bp']['ss1'])
    geometry.addCell(pincells[group][name]['bp']['water'])
    geometry.addCell(pincells[group][name]['bp']['cladding'])
    geometry.addCell(pincells[group][name]['bp']['water1'])    

geometry.addCell(assembly16)
geometry.addCell(assembly24)
geometry.addCell(core)

# add lattices
geometry.addLattice(lattices[group]['1.6-0BP'])
geometry.addLattice(lattices[group]['2.4-16BP'])
geometry.addLattice(smallcore)

#initialize flat source regions
geometry.initializeFlatSourceRegions()

num_azims = [i for i in range(4, 128, 4)]

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
	
	process.store_simulation_state(solver, pin_powers=True, use_hdf5=True, \
																filename= "simstate160.h5", append=True)
																

