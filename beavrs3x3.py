from pincells import pincells
from lattices import lattices, pinPitch
from materials import materials
from openmoc import *
import openmoc.log as log
from surfaces import surfaces
import openmoc.plotter as plotter

groups = input('How many energy groups?')
if groups == '2' or groups == 2:
  group = '2'
elif groups == '8' or groups == 8:
  group = '8'

assembly16 = CellFill(universe=universe_id(), universe_fill= lattices[group]['1.6-0BP'].getId())
assembly24 = CellFill(universe=universe_id(), universe_fill= lattices[group]['2.4-16BP'].getId())


id16 = assembly16.getUniverseId()
id24 = assembly24.getUniverseId()


smallcore = Lattice(id=universe_id(), width_x = pinPitch*17, width_y = pinPitch*17)
smallcore.setLatticeCells([[id16, id24, id16],
                          [id24, id16, id24],
                          [id16, id24, id16]])
                          
master_cell = CellFill(universe=0, universe_fill = smallcore.getId())

#create surfaces
left = openmoc.XPlane(x=-pinPitch*17*3/2.0)
right = openmoc.XPlane(x=pinPitch*17*3/2.0)
bottom = openmoc.YPlane(y=-pinPitch*17*3/2.0)
top = openmoc.YPlane(y=pinPitch*17*3/2.0)


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

names = ['pwru160c00','pwru240w16']
bps = ['pwru240w12', 'pwru240w16', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

for surface in surfaces:
	geometry.addSurface(surfaces[surface])

geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(top)
geometry.addSurface(bottom)


for name in names:
  if name in bps:
    materialtypes = ['fuel', 'cladding', 'helium', 'water', 'ss304', 'bp']
  else:
    materialtypes = ['fuel', 'cladding', 'helium', 'water']
  for material in materialtypes:
    #add materials
    geometry.addMaterial(materials[group][name][material])

for name in names:
  #add ALL cells
  geometry.addCell(pincells[group][name]['fuel'])
  geometry.addCell(pincells[group][name]['cladding'])
  geometry.addCell(pincells[group][name]['water'])
  geometry.addCell(pincells[group][name]['helium'])
  #guidetube
  geometry.addCell(pincells[group][name]['guidetube']['water1'])
  geometry.addCell(pincells[group][name]['guidetube']['water2'])
  geometry.addCell(pincells[group][name]['guidetube']['cladding'])
  #instrumenttube
  geometry.addCell(pincells[group][name]['instube']['helium'])
  geometry.addCell(pincells[group][name]['instube']['cladding1'])
  geometry.addCell(pincells[group][name]['instube']['cladding2'])
  geometry.addCell(pincells[group][name]['instube']['water1'])
  geometry.addCell(pincells[group][name]['instube']['water2'])
  
  
  print 'finished 1st lattice cells'
  if name in bps:
    #bp
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
print 'almost done'
geometry.addCell(master_cell)


#add all lattices
geometry.addLattice(lattices[group]['1.6-0BP'])
geometry.addLattice(lattices[group]['2.4-16BP'])
geometry.addLattice(smallcore)


#initialize flat source regions
geometry.initializeFlatSourceRegions()


# Initialize the track generator after the geometry has been
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
solver.printTimerReport()

#plot geometry by materials, cells, and FSRs
plotter.plot_cells(geometry)
plotter.plot_materials(geometry)
plotter.plot_flat_source_regions(geometry)
plotter.plot_fluxes(geometry, solver)
