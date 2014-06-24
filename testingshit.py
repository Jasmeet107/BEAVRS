from pincells import pincells
from lattices import lattices, pinPitch
from materials import materials
from openmoc import *
import openmoc.log as log

log.set_log_level('DEBUG')

groups = input('How many energy groups?')
if groups == '2' or groups == 2:
  group = '2'
elif groups == '8' or groups == 8:
  group = '8'

onecell = pincells[group]['pwru160c00']['fuel']

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
onecell.addSurface(halfspace=+1, surface=left)
onecell.addSurface(halfspace=-1, surface=right)
onecell.addSurface(halfspace=+1, surface=bottom)
onecell.addSurface(halfspace=-1, surface=top)

geometry = Geometry() #initialize geometry

#add materials
geometry.addMaterial(materials[group]['pwru160c00']['fuel'])

#add ALL cells
geometry.addCell(pincells[group]['pwru160c00']['fuel'])

#initialize flat source regions
geometry.initializeFlatSourceRegions()
