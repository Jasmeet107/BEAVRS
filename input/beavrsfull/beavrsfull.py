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
group = '8'

log.set_log_level('NORMAL')

log.py_printf('TITLE', 'Simulating the BEAVRS full core benchmark...')

###############################################################################
###########################   Creating Surfaces   #############################
###############################################################################

log.py_printf('NORMAL', 'Creating surfaces...')

left = openmoc.XPlane(x=-267.716)
right = openmoc.XPlane(x=267.716)
bottom = openmoc.YPlane(y=-267.716)
top = openmoc.YPlane(y=267.716)

left.setBoundaryType(VACUUM)
right.setBoundaryType(VACUUM)
bottom.setBoundaryType(VACUUM)
top.setBoundaryType(VACUUM)

core_cylinders = []
core_cylinders.append(Circle(x=0., y=0., radius=187.960))
core_cylinders.append(Circle(x=0., y=0., radius=193.675))
core_cylinders.append(Circle(x=0., y=0., radius=199.39))
core_cylinders.append(Circle(x=0., y=0., radius=230.0))
core_cylinders.append(Circle(x=0., y=0., radius=251.9))

neutron_shield_planes = []
neutron_shield_planes.append(Plane(A=-0.577350, B=1.0, C=0.))
neutron_shield_planes.append(Plane(A=-1.732051, B=1.0, C=0.))
neutron_shield_planes.append(Plane(A=1.732051, B=1.0, C=0.))
neutron_shield_planes.append(Plane(A=0.577350, B=1.0, C=0.))

###############################################################################
#############################   Creating Cells   ##############################
###############################################################################

log.py_printf('NORMAL', 'Creating cells...')

water = CellFill(universe=universe_id(), universe_fill=lattices[group]['water'].getId())
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

core_cells = []

# assembly lattice
core_cells.append(CellFill(universe = 0, universe_fill = 10))
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[0])

# core barrel
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['ss304'].getId(), rings=3, sectors=16))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[0])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[1])

# neutron shield northeast
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['ss304'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[0])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[1])

# neutron shield northwest
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['ss304'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[2])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[3])

# neutron shield southwest
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['ss304'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[0])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[1])

# neutron shield southest
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['ss304'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[2])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[3])

# water jacket east
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[0])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[3])

# water jacket northeast
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[0])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[1])

# water jacket north
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[1])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[2])

# water jacket northwest
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[2])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[3])

# water jacket west
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[0])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[3])

# water jacket southwest
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[0])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[1])

# water jacket south
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[1])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[1])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[2])

# water jacket southeast
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru160c00']['water'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[2])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=-1, surface=neutron_shield_planes[2])
core_cells[-1].addSurface(halfspace=+1, surface=neutron_shield_planes[3])

# pressure vessel
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['ss304'].getId(), rings=3, sectors=16))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[3])
core_cells[-1].addSurface(halfspace=-1, surface=core_cylinders[4])

# vacuum outside pressure vessel
core_cells.append(CellBasic(universe = 0, material=materials[group]['pwru240w12']['helium'].getId()))
core_cells[-1].addSurface(halfspace=+1, surface=core_cylinders[4])
core_cells[-1].addSurface(halfspace=+1, surface=left)
core_cells[-1].addSurface(halfspace=-1, surface=right)
core_cells[-1].addSurface(halfspace=+1, surface=bottom)
core_cells[-1].addSurface(halfspace=-1, surface=top)

###############################################################################
###########################   Creating Lattices   #############################
###############################################################################

log.py_printf('NORMAL', 'Creating lattices...')

w = water.getUniverseId()
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

fullcore = Lattice(10, pin_pitch*17, pin_pitch*17)
fullcore.setLatticeCells([[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, c, d, c, d, c, d, c, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, c, c, o, a, p, a, p, a, o, c, c, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, c, j, n, a, n, a, n, a, n, a, n, m, c, w, w, w, w, w, w],
                          [w, w, w, w, w, w, c, n, b, n, a, h, a, h, a, n, b, n, c, w, w, w, w, w, w],
                          [w, w, w, w, w, c, o, a, n, a, h, a, h, a, h, a, n, a, o, c, w, w, w, w, w],
                          [w, w, w, w, w, e, a, n, a, h, a, h, a, h, a, h, a, n, a, f, w, w, w, w, w],
                          [w, w, w, w, w, c, p, a, h, a, h, a, n, a, h, a, h, a, p, c, w, w, w, w, w],
                          [w, w, w, w, w, e, a, n, a, h, a, n, a, n, a, h, a, n, a, f, w, w, w, w, w],
                          [w, w, w, w, w, c, p, a, h, a, h, a, n, a, h, a, h, a, p, c, w, w, w, w, w],
                          [w, w, w, w, w, e, a, n, a, h, a, h, a, h, a, h, a, n, a, f, w, w, w, w, w],
                          [w, w, w, w, w, c, o, a, n, a, h, a, a, a, h, a, n, a, o, c, w, w, w, w, w],
                          [w, w, w, w, w, w, c, n, b, n, a, h, a, h, a, n, b, n, c, w, w, w, w, w, w],
                          [w, w, w, w, w, w, c, k, n, a, n, a, n, a, n, a, n, l, c, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, c, c, o, a, p, a, p, a, o, c, c, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, c, g, c, g, c, g, c, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                          [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]])


###############################################################################
##########################     Creating Cmfd mesh    ##########################
###############################################################################

log.py_printf('NORMAL', 'Creating Cmfd mesh...')

cmfd = Cmfd()
cmfd.setLatticeStructure(25,25)

###############################################################################
##########################   Creating the Geometry   ##########################
###############################################################################

log.py_printf('NORMAL', 'Creating geometry...')

geometry = Geometry(cmfd)

names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']
bps = ['pwru240w12', 'pwru240w16', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

# add surfaces
for surface in surfaces:
  geometry.addSurface(surfaces[surface])

for surface in core_cylinders:
  geometry.addSurface(surface)

for surface in neutron_shield_planes:
  geometry.addSurface(surface)

geometry.addSurface(left)
geometry.addSurface(right)
geometry.addSurface(bottom)
geometry.addSurface(top)

# add materials
for name in names:
  if name in bps:
    materialtypes = ['fuel', 'cladding', 'helium', 'water', 'ss304', 'bp']
  else:
    materialtypes = ['fuel', 'cladding', 'helium', 'water']
  for material in materialtypes:
    #add materials
    geometry.addMaterial(materials[group][name][material])

# add cells
for name in names:

  geometry.addCell(pincells[group][name]['fuel'])
  geometry.addCell(pincells[group][name]['cladding'])
  geometry.addCell(pincells[group][name]['water'])
  geometry.addCell(pincells[group][name]['helium'])

  #guidetube
  geometry.addCell(pincells[group][name]['guidetube']['water1'])
  geometry.addCell(pincells[group][name]['guidetube']['water2'])
  geometry.addCell(pincells[group][name]['guidetube']['cladding'])

  #instrument tube
  geometry.addCell(pincells[group][name]['instube']['helium'])
  geometry.addCell(pincells[group][name]['instube']['cladding1'])
  geometry.addCell(pincells[group][name]['instube']['cladding2'])
  geometry.addCell(pincells[group][name]['instube']['water1'])
  geometry.addCell(pincells[group][name]['instube']['water2'])
  
  # burnable poisons
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
    
geometry.addCell(water)
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

for cell in core_cells:
  geometry.addCell(cell)

# add all lattices
geometry.addLattice(lattices[group]['water'])
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

# initialize flat source regions
geometry.initializeFlatSourceRegions()

# plot geometry materials and cells
plotter.plot_cells(geometry, gridsize=1000)
plotter.plot_materials(geometry, gridsize=1000)

###############################################################################
########################   Creating the TrackGenerator   ######################
###############################################################################

log.py_printf('NORMAL', 'Initializing the track generator...')

track_generator = ModularTrackGenerator(geometry, num_azim, track_spacing)
track_generator.setLatticeStructure(1,1)
track_generator.generateTracks()

plotter.plot_flat_source_regions(geometry, gridsize=1000)

###############################################################################
###########################   Running a Simulation   ##########################
###############################################################################

solver = ModularCPUSolver(geometry, track_generator)
solver.setSourceConvergenceThreshold(tolerance)
solver.setNumThreads(num_threads)
solver.convergeSource(max_iters)
solver.printTimerReport()

###############################################################################
############################   Generating Plots   #############################
###############################################################################

log.py_printf('NORMAL', 'Plotting data...')

plotter.plot_fluxes(geometry, solver, energy_groups=[1,2,3,4,5,6,7,8], gridsize=1000)
