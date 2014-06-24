from pincells import pincells
from lattices import lattices, pinPitch
from openmoc import *

assembly = CellFill(universe=universe_id(), universe_fill= lattices['3.1-15bBP'].getId()) #create cell, fill with lattice

#create surfaces
left = openmoc.XPlane(x=-pinPitch*17/2.0)
right = openmoc.XPlane(x=pinPitch*17/2.0)
bottom = openmoc.YPlane(y=-pinPitch*17/2.0)
top = openmoc.YPlane(y=pinPitch*17/2.0)

#sets boundary condition to be reflective
left.setBoundaryType(REFLECTIVE)
right.setBoundaryType(REFLECTIVE)
bottom.setBoundaryType(REFLECTIVE)
top.setBoundaryType(REFLECTIVE)

#add surfaces to bound cell
assembly.addSurface(halfspace=+1, left)
assembly.addSurface(halfsapce=-1, right)
assembly.addSurface(halfspace=+1, bottom)
assembly.addSurface(halfspace=-1, top)

geometry = Geometry() #initialize geometry

#add materials
geometry.addMaterial(materials['a'])
geometry.addMaterial(materials['b'])
geometry.addMaterial(materials['c'])

#add ALL cells

#fuel
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
geometry.addLattice(lattices['3.1-15bBP'])

#initialize flat source regions
geometry.initializeFlatSourceRegions()
