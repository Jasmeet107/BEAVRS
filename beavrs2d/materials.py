from generatehdf5 import generate
import openmoc.materialize as materialize
import os

assembly_names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']
group_types = ['2-group/','8-group/']

materials = {}


# create materials for each assembly and number of groups
for group in group_types:
  materials[group[0]] = {}
  for name in assembly_names:
    if not os.path.isfile('casmo-data/'+ group[0] + '-group/' + name + '-avg-materials.hdf5'):
      generate([name], [group])
      ## only runs when these files don't exist already!! 

    materials[group[0]][name] = materialize.materialize('casmo-data/'+ group[0] + '-group/' + name + '-avg-materials.hdf5')
