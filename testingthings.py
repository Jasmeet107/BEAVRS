from openmoc import *
from materials import materials
import openmoc.log as log

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

geometry.initializeFlatSourceRegions()
