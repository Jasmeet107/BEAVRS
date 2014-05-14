from openmoc.compatible.casmo import *
assemblies = 
casmo = Casmo()
casmo.setCellType(1,'fuel')
casmo.setCellType(2,'gt')
casmo.setCellType(3,'bp')
casmo.setFileName('c4.pwru160c00.out')
casmo.setDirectory('Cross-Section-Output/2-group/')
casmo.importEnergyGroups()
print casmo._energy_groups
casmo.importFromCasmo('c4.pwru160c00.out','Cross-Section-Output/2-group/')
casmo.setStringCellTypeArray(casmo.stringCellTypeArray())
casmo.averageXSGenerator()
casmo.exportAvgXSToHDF5('pwru160c00','casmo-data/2-group/')
print casmo._average_cross_sections
