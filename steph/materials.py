assembly_names = ['pwru160c00','pwru240c00','pwru240w12','pwru310c00','pwru310w12']
materials = {}
for name in assembly_names:
    materials[name] = materialize.materialize('casmo-data/' + name + '-materials.hdf5')
