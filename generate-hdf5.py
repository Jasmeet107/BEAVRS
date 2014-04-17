from casmo.py import *

assembly_names = ['pwru160c00','pwru240c00','pwru240w12','pwru310c00','pwru310w12']
for name in assembly_names:
    assembly = Casmo()
    #note--ask Will about setting directory and filename
    assembly.setDirectory('/casmo-reference')
    assembly.setFilename('c4.' + name + '.out')
    assembly.importAllXS()
    assembly.xsToHDF5(name)
