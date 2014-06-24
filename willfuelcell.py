from pincells import pincells
from materials import materials
from lattices import pinPitch
from openmoc import *
import openmoc.log as log
from surfaces import surfaces
import openmoc.plotter as plotter

log.set_log_level('DEBUG')

groups = input('How many energy groups?')
if groups == '2' or groups == 2:
  group = '2'
elif groups == '8' or groups == 8:
  group = '8'

lattice = Lattice(universe_id(), width_x=pinPitch, width_y=pinPitch)

master_cell = CellFill(universe=0, universe_fill=lattice.getId())

lattice.setLatticeCells([[pincells[group]['pwru160c00']['uid']]])

#create surfaces
left = openmoc.XPlane(x=-pinPitch/2.0)
right = openmoc.XPlane(x=pinPitch/2.0)
bottom = openmoc.YPlane(y=-pinPitch/2.0)
top = openmoc.YPlane(y=pinPitch/2.0)

#sets boundary condition to be reflective
left.setBoundaryType(REFLECTIVE)
right.setBoundaryType(REFLECTIVE)
bottom.setBoundaryType(REFLECTIVE)
top.setBoundaryType(REFLECTIVE)

#add surfaces to bound cell
master_cell.addSurface(halfspace=+1, surface=left)
master_cell.addSurface(halfspace=-1, surface=right)
master_cell.addSurface(halfspace=+1, surface=bottom)
master_cell.addSurface(halfspace=-1, surface=top)

geometry = Geometry() #initialize geometry

#add materials
materialtypes = ['fuel', 'helium', 'cladding', 'water']
for material in materialtypes:
  geometry.addMaterial(materials[group]['pwru160c00'][material])

#add surfaces
geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(bottom)
geometry.addSurface(top)
geometry.addSurface(surfaces['Fuel Radius-1'])
geometry.addSurface(surfaces['Fuel Radius-2'])
geometry.addSurface(surfaces['Fuel Radius-3'])


#add ALL cells
geometry.addCell(pincells[group]['pwru160c00']['fuel'])
geometry.addCell(pincells[group]['pwru160c00']['helium'])
geometry.addCell(pincells[group]['pwru160c00']['cladding'])
geometry.addCell(pincells[group]['pwru160c00']['water'])
#geometry.addCell(pincells[group]['pwru160c00']['guidetube']['water'])
#geometry.addCell(pincells[group]['pwru160c00']['guidetube']['cladding'])
#geometry.addCell(pincells[group]['pwru160c00']['instube']['helium'])
#geometry.addCell(pincells[group]['pwru160c00']['instube']['cladding'])
geometry.addCell(master_cell)

#add all lattices
geometry.addLattice(lattice)


#initialize flat source regions
geometry.initializeFlatSourceRegions()

#plot geometry by materials, cells, and FSRs
plotter.plot_cells(geometry)
#plotter.plot_materials(geometry)
#plotter.plot_flat_source_regions(geometry)

'''# Initialize the track generator after the geometry has been
# constructed. Use 64 azimuthal angles and 0.05 cm track spacing.
track_generator = openmoc.TrackGenerator(geometry, num_azim=64, \
                                         spacing=0.05)

# Generate tracks using ray tracing across the geometry
track_generator.generateTracks()

# Initialize a solver for the simulation and set the number of
# threads and source convergence threshold
solver = openmoc.ThreadPrivateSolver(geometry, track_generator)
solver.setNumThreads(4)
solver.setSourceConvergenceThreshold(1E-5)

# Converge the source with up to a maximum of 1000 source iterations
solver.convergeSource(1000)

# Print a report of the time to solution
solver.printTimerReport()'''
