from pincells import pincells
from lattices import lattices, pinPitch
from openmoc import *

assembly16 = CellFill(universe=universe_id(), universe_fill= lattices['1.6-0BP'].getId()) 
assembly24 = CellFill(universe=universe_id(), universe_fill= lattices['2.4-16BP'].getId())
id16 = assembly16.getId()
id24 = assembly24.getId()
smallcore = Lattice(id=universe_id(), width_x = pinPitch*17, width_y = pinPitch*17)
smallcore.setLatticeCells([[id16, id24, id16],
                          [id24, id16, id24],
                          [id16, id24, id16]])

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
geometry.addLattice(lattices['2.4-16BP'])
geometry.addLattice(smallcore)

#initialize flat source regions
geometry.initializeFlatSourceRegions()
