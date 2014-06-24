from openmoc import *
from materials import materials
import openmoc.log as log

log.set_log_level('DEBUG')

water = CellBasic(universe=universe_id(), material= materials['2']['pwru160c00']['water'].getId())

pinPitch = 1.25984

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



### ADDED BY WILL
lattice = Lattice(universe_id(), width_x=pinPitch, width_y=pinPitch)
master_cell = CellFill(universe=0, universe_fill=lattice.getId())
lattice.setLatticeCells([[water.getUniverseId()]])



#add surfaces to bound cell
water.addSurface(halfspace=+1, surface=left)
water.addSurface(halfspace=-1, surface=right)
water.addSurface(halfspace=+1, surface=bottom)
water.addSurface(halfspace=-1, surface=top)

geometry = Geometry()

geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(bottom)
geometry.addSurface(top)
geometry.addMaterial(materials['2']['pwru160c00']['water'])
geometry.addCell(water)



### ADDED BY WILL
geometry.addCell(master_cell)
geometry.addLattice(lattice)



geometry.initializeFlatSourceRegions()



### ADDED BY WILL
import openmoc.plotter as plotter
plotter.plot_cells(geometry)
plotter.plot_materials(geometry)
plotter.plot_flat_source_regions(geometry)

