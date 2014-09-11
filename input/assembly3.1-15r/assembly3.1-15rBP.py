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

log.py_printf('TITLE', 'Simulating the BEAVRS 1.6 pct enriched 0 BP assembly...')
  
group = '8'
assembly = CellFill(universe=0, universe_fill= lattices[group]['3.1-15rBP'].getId()) #create cell, fill with lattice

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
  geometry.addMaterial(materials[group]['pwru310w15'][material])

#add surfaces
geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(bottom)
geometry.addSurface(top)

for surface in surfaces:
  geometry.addSurface(surfaces[surface])


#add cells
geometry.addCell(pincells[group]['pwru310w15']['fuel'])
geometry.addCell(pincells[group]['pwru310w15']['cladding'])
geometry.addCell(pincells[group]['pwru310w15']['water'])
geometry.addCell(pincells[group]['pwru310w15']['helium'])
geometry.addCell(pincells[group]['pwru310w15']['guidetube']['water1'])
geometry.addCell(pincells[group]['pwru310w15']['guidetube']['water2'])
geometry.addCell(pincells[group]['pwru310w15']['guidetube']['cladding'])
geometry.addCell(pincells[group]['pwru310w15']['instube']['cladding1'])
geometry.addCell(pincells[group]['pwru310w15']['instube']['helium'])
geometry.addCell(pincells[group]['pwru310w15']['instube']['cladding2'])
geometry.addCell(pincells[group]['pwru310w15']['instube']['water1'])
geometry.addCell(pincells[group]['pwru310w15']['instube']['water2'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['helium'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['ss'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['helium1'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['bg'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['helium2'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['ss1'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['water'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['cladding'])
geometry.addCell(pincells[group]['pwru310w15']['bp']['water1'])
geometry.addCell(assembly)

#add pincell lattice
geometry.addLattice(lattices[group]['3.1-15rBP'])

#initialize flat source regions
geometry.initializeFlatSourceRegions()

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

###############################################################################
############################   Generating Plots   #############################
###############################################################################

log.py_printf('NORMAL', 'Plotting data...')

plotter.plot_cells(geometry)
plotter.plot_materials(geometry)
plotter.plot_flat_source_regions(geometry)
plotter.plot_fluxes(geometry, solver, energy_groups=[1,2,3,4,5,6,7,8])

