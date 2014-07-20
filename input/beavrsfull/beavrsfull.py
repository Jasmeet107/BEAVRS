from beavrs2d import *
from beavrs2d.lattices import pinPitch
from openmoc import *
import openmoc.log as log
import openmoc.plotter as plotter

#log.set_log_level('DEBUG')

# groups = input('How many energy groups?')
# if groups == '2' or groups == 2:
#   group = '2'
# elif groups == '8' or groups == 8:
#   group = '8'
  
group = '2'
group = '8' #default

a160 = CellFill(universe=universe_id(), universe_fill= lattices[group]['1.6-0BP'].getId())
b240 = CellFill(universe=universe_id(), universe_fill= lattices[group]['2.4-0BP'].getId())
c310 = CellFill(universe= universe_id(), universe_fill=lattices[group]['3.1-0BP'].getId())
d316t = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-6tBP'].getId())
e316l = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-6lBP'].getId())
f316r = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-6rBP'].getId())
g316b = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-6bBP'].getId())
h2412 = CellFill(universe=universe_id(), universe_fill= lattices[group]['2.4-12BP'].getId())
i3112 = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-12BP'].getId())
j3115t = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-15tBP'].getId())
k3115l = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-15lBP'].getId())
l3115r = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-15rBP'].getId())
m3115b = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-15bBP'].getId())
n2416 = CellFill(universe=universe_id(), universe_fill= lattices[group]['2.4-16BP'].getId())
o3116 = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-16BP'].getId())
p3120 = CellFill(universe=universe_id(), universe_fill= lattices[group]['3.1-20BP'].getId())

w = pincells[group]['water'].getUniverseId()
a = a160.getUniverseId()
b = b240.getUniverseId()
c = c310.getUniverseId()
d = d316t.getUniverseId()
e = e316l.getUniverseId()
f = f316r.getUniverseId()
g = g316b.getUniverseId()
h = h2412.getUniverseId()
i = i3112.getUniverseId()
j = j3115t.getUniverseId()
k = k3115l.getUniverseId()
l = l3115r.getUniverseId()
m = m3115b.getUniverseId()
n = n2416.getUniverseId()
o = o3116.getUniverseId()
p = p3120.getUniverseId()


fullcore = Lattice(id=universe_id(), width_x = pinPitch*17, width_y = pinPitch*17)
fullcore.setLatticeCells([[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, c, d, c, d, c, d, c, w, w, w, w, w],
                          [w, w, w, c, c, o, a, p, a, p, a, o, c, c, w, w, w],
                          [w, w, c, j, n, a, n, a, n, a, n, a, n, m, c, w, w],
                          [w, w, c, n, b, n, a, h, a, h, a, n, b, n, c, w, w],
                          [w, c, o, a, n, a, h, a, h, a, h, a, n, a, o, c, w],
                          [w, e, a, n, a, h, a, h, a, h, a, h, a, n, a, f, w],
                          [w, c, p, a, h, a, h, a, n, a, h, a, h, a, p, c, w],
                          [w, e, a, n, a, h, a, n, a, n, a, h, a, n, a, f, w],
                          [w, c, p, a, h, a, h, a, n, a, h, a, h, a, p, c, w],
                          [w, e, a, n, a, h, a, h, a, h, a, h, a, n, a, f, w],
                          [w, c, o, a, n, a, h, a, a, a, h, a, n, a, o, c, w],
                          [w, w, c, n, b, n, a, h, a, h, a, n, b, n, c, w, w],
                          [w, w, c, k, n, a, n, a, n, a, n, a, n, l, c, w, w],
                          [w, w, w, c, c, o, a, p, a, p, a, o, c, c, w, w, w],
                          [w, w, w, w, w, c, g, c, g, c, g, c, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]])

fullcorecell = CellFill(universe = 0, universe_fill = fullcore.getId())

#create surfaces
left = openmoc.XPlane(x=-pinPitch*17*17/2.0)
right = openmoc.XPlane(x=pinPitch*17*17/2.0)
bottom = openmoc.YPlane(y=-pinPitch*17*17/2.0)
top = openmoc.YPlane(y=pinPitch*17*17/2.0)

#sets boundary condition to be reflective
left.setBoundaryType(REFLECTIVE)
right.setBoundaryType(REFLECTIVE)
bottom.setBoundaryType(REFLECTIVE)
top.setBoundaryType(REFLECTIVE)

#add surfaces to bound cell
fullcorecell.addSurface(halfspace=+1, surface=left)
fullcorecell.addSurface(halfspace=-1, surface=right)
fullcorecell.addSurface(halfspace=+1, surface=bottom)
fullcorecell.addSurface(halfspace=-1, surface=top)

geometry = Geometry() #initialize geometry

names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']
bps = ['pwru240w12', 'pwru240w16', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

for surface in surfaces:
	geometry.addSurface(surfaces[surface])

geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(bottom)
geometry.addSurface(top)

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
    

geometry.addCell(a160)
geometry.addCell(b240)
geometry.addCell(c310)
geometry.addCell(d316t)
geometry.addCell(e316l)
geometry.addCell(f316r)
geometry.addCell(g316b)
geometry.addCell(h2412)
geometry.addCell(i3112)
geometry.addCell(j3115t)
geometry.addCell(k3115l)
geometry.addCell(l3115r)
geometry.addCell(m3115b)
geometry.addCell(n2416)
geometry.addCell(o3116)
geometry.addCell(p3120)
geometry.addCell(pincells[group]['water'])
geometry.addCell(fullcorecell)



#add all lattices

geometry.addLattice(lattices[group]['1.6-0BP'])
geometry.addLattice(lattices[group]['2.4-0BP'])
geometry.addLattice(lattices[group]['3.1-0BP'])
geometry.addLattice(lattices[group]['3.1-6tBP'])
geometry.addLattice(lattices[group]['3.1-6rBP'])
geometry.addLattice(lattices[group]['3.1-6lBP'])
geometry.addLattice(lattices[group]['3.1-6bBP'])
geometry.addLattice(lattices[group]['2.4-12BP'])
geometry.addLattice(lattices[group]['3.1-12BP'])
geometry.addLattice(lattices[group]['3.1-15tBP'])
geometry.addLattice(lattices[group]['3.1-15rBP'])
geometry.addLattice(lattices[group]['3.1-15lBP'])
geometry.addLattice(lattices[group]['3.1-15bBP'])
geometry.addLattice(lattices[group]['2.4-16BP'])
geometry.addLattice(lattices[group]['3.1-16BP'])
geometry.addLattice(lattices[group]['3.1-20BP'])
geometry.addLattice(fullcore)

#initialize flat source regions
geometry.initializeFlatSourceRegions()

#plot geometry by materials, cells, and FSRs
plotter.plot_cells(geometry)
plotter.plot_materials(geometry)
plotter.plot_flat_source_regions(geometry)

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

#Plot fluxes
plotter.plot_fluxes(geometry, solver, energy_groups=[1, 2, 3, 4, 5, 6, 7, 8])