from casmo import *

assembly_names = ['pwru160c00','pwru240c00','pwru240w12','pwru310c00','pwru310w12']
group_types =['2-group/','8-group/']
for name in assembly_names:
    for group in group_types:
        assembly = Casmo()
        assembly.importFromCASMO('c4.' + name + '.out','Cross-Section-Output/'+group)
        assembly.xsToHDF5(name,directory = 'casmo-data/'+group)
