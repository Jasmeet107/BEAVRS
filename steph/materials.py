import openmoc.materialize as materialize

assembly_names = ['pwru160c00','pwru240c00','pwru240w12','pwru310c00','pwru310w12']
group_names=['2-group/','8-group/']
materials = {}
for name in assembly_names:
    materials[name]={}
    for group in group_names:
        materials[name][group] = materialize.materialize('casmo-data/'+group + name + '-materials.hdf5')
