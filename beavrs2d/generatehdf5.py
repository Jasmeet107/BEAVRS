from openmoc.compatible.casmo import *
import os


cwd = os.path.dirname(os.path.abspath(__file__))


def generate (assembly_names, group_types): 
	print "GENERATING"
	for name in assembly_names:
			for group in group_types:
					assembly = Casmo()
					assembly.setCellType(1,'fuel')
					assembly.setCellType(2,'gt')
					assembly.setCellType(3,'bp')        
					assembly.importFromCasmo('c4.' + name + '.txt', cwd + '/Cross-Section-Output/'+group)
					fiss_xs = assembly.getXS('SIGF')
					chi = numpy.zeros((assembly.getNumRegions(),assembly.getEnergyGroups()))
					for region in range(assembly.getNumRegions()):
							fiss_sum = sum(fiss_xs[region,:])
						
							if fiss_sum > 0:
									if assembly.getEnergyGroups() == 2:
											chi[region,:] = numpy.array([1,0])
									if assembly.getEnergyGroups() == 8:
											chi[region,:] = numpy.array([7.560E-01, 2.438E-01, 1.808E-04, 0.000E+00, 0.000E+00, 0.000E+00,
	0.000E+00, 0.000E+00])
					print chi
					assembly.setXS('CHI', chi)
					assembly.setStringCellTypeArray(assembly.stringCellTypeArray())
					assembly.exportAllXSToHDF5(name,directory = 'casmo-data/'+group)
					assembly.averageXSGenerator()
					assembly.exportAvgXSToHDF5(name,directory = 'casmo-data/'+group)


#assembly_names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']
#group_types =['2-group/','8-group/']



'''comments'''

        
