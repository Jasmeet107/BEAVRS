from pincells import pincells
from lattices import lattices, pinPitch
from openmoc import *



a160 = CellFill(universe=universe_id(), universe_fill= lattices['1.6-0BP'].getId()) 
b240 = CellFill(universe=universe_id(), universe_fill= lattices['2.4-0BP'].getId())
c310 = CellFill(universe=universe_id(), universe_fill= lattices['3.1-0BP'].getId())
d316t = CellFill(universe=universe_id(), universe_fill= lattices['3.1-6tBP'].getId())
e316l = CellFill(universe=universe_id(), universe_fill= lattices['3.1-6lBP'].getId())
f316r = CellFill(universe=universe_id(), universe_fill= lattices['3.1-6rBP'].getId())
g316b = CellFill(universe=universe_id(), universe_fill= lattices['3.1-6bBP'].getId())
h2412 = CellFill(universe=universe_id(), universe_fill= lattices['2.4-12BP'].getId())
i3112 = CellFill(universe=universe_id(), universe_fill= lattices['3.1-12BP'].getId())
j3115t = CellFill(universe=universe_id(), universe_fill= lattices['3.1-15tBP'].getId()) 
k3115l = CellFill(universe=universe_id(), universe_fill= lattices['3.1-15lBP'].getId())
l3115r = CellFill(universe=universe_id(), universe_fill= lattices['3.1-15rBP'].getId())
m3115b = CellFill(universe=universe_id(), universe_fill= lattices['3.1-15bBP'].getId())
n2416 = CellFill(universe=universe_id(), universe_fill= lattices['2.4-16BP'].getId())
o3116 = CellFill(universe=universe_id(), universe_fill= lattices['3.1-16BP'].getId())
p3120 = CellFill(universe=universe_id(), universe_fill= lattices['3.1-20BP'].getId())

w = pincells['water']['uid']
a = a160.getId()
b = b240.getId()
c = c310.getId()
d = d316t.getId()
e = e316l.getId()
f = f316r.getId()
g = g316b.getId()
h = h2412.getId()
i = i3112.getId()
j = j3115t.getId()
k = k3115l.getId()
l = l3115r.getId()
m = m3115b.getId()
n = n2416.getId()
o = o3116.getId()
p = p3120.getId()


fullcore = Lattice(id=universe_id(), width_x = pinPitch*17*17, width_y = pinPitch*17*17)
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
smallcore.addSurface(halfspace=+1, left)
smallcore.addSurface(halfsapce=-1, right)
smallcore.addSurface(halfspace=+1, bottom)
smallcore.addSurface(halfspace=-1, top)

geometry = Geometry() #initialize geometry

#add materials
geometry.addMaterial(materials['a'])
geometry.addMaterial(materials['b'])
geometry.addMaterial(materials['c'])

#add ALL cells

#16fuel
geometry.addCell(pincells['16fuel']['fuel'])
geometry.addCell(pincells['16fuel']['clad'])
geometry.addCell(pincells['16fuel']['water'])
#24fuel
geometry.addCell(pincells['24fuel']['fuel'])
geometry.addCell(pincells['24fuel']['clad'])
geometry.addCell(pincells['24fuel']['water'])
#31fuel
geometry.addCell(pincells['31fuel']['fuel'])
geometry.addCell(pincells['31fuel']['clad'])
geometry.addCell(pincells['31fuel']['water'])
#guidetube
geometry.addCell(pincells['guidetube']['water'])  
geometry.addCell(pincells['guidetube']['clad'])
#instrumenttube
geometry.addCell(pincells['instube']['air'])
geometry.addCell(pincells['instube']['clad'])
#bp
geometry.addCell(pincells['bp']['air'])
geometry.addCell(pincells['bp']['ss'])
geometry.addCell(pincells['bp']['air1'])
geometry.addCell(pincells['bp']['bg'])
geometry.addCell(pincells['bp']['air2'])
geometry.addCell(pincells['bp']['ss1'])
geometry.addCell(pincells['bp']['water'])
geometry.addCell(pincells['bp']['clad'])

#add all lattices
geometry.addLattice(lattices['1.6-0BP'])
geometry.addLattice(lattices['2.4-0BP'])
geometry.addLattice(lattices['3.1-0BP'])
geometry.addLattice(lattices['3.1-6tBP'])
geometry.addLattice(lattices['3.1-6rBP'])
geometry.addLattice(lattices['3.1-6lBP'])
geometry.addLattice(lattices['3.1-6bBP'])
geometry.addLattice(lattices['2.4-12BP'])
geometry.addLattice(lattices['3.1-12BP'])
geometry.addLattice(lattices['3.1-15tBP'])
geometry.addLattice(lattices['3.1-15rBP'])
geometry.addLattice(lattices['3.1-15lBP'])
geometry.addLattice(lattices['3.1-15bBP'])
geometry.addLattice(lattices['2.4-16BP'])
geometry.addLattice(lattices['3.1-16BP'])
geometry.addLattice(lattices['3.1-20BP'])
geometry.addLattice(fullcore)

#initialize flat source regions
geometry.initializeFlatSourceRegions()
