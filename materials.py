import openmoc.materialize as materialize

assembly_names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']
group_names=['2','8']
materials = {}
for group in group_names:
  materials[group]={}
  for name in assembly_names:
    materials[group][name] = materialize.materialize('casmo-data/'+ group + '-group/' + name + '-avg-materials.hdf5')

