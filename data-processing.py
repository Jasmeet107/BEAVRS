import h5py
import numpy
import matplotlib.pyplot as plt

assemblies = ['assembly1.6-0', 'assembly2.4-0', 'assembly2.4-12', 'assembly2.4-16', 'assembly3.1-0', 'assembly3.1-6b', 'assembly3.1-6l', 'assembly3.1-6r', 'assembly3.1-6t', 'assembly3.1-12', 'assembly3.1-15b', 'assembly3.1-15l', 'assembly3.1-15r', 'assembly3.1-15t', 'assembly3.1-20']

num_cases = 31
for assembly in assemblies: 

	directory = 'studies/' + assembly + '/simulation-states/' 
	filename = directory + 'simulation-state.h5'

	#finds kinf from simulation for all cases
	f = h5py.File(filename)
	all_kinf = numpy.zeros((num_cases))
	all_azim = numpy.zeros((num_cases))
	dates = f.keys()
	for date in dates: 
		timestamps = f[date].keys()
		for timestamp in timestamps: 
			calculated_kinf = f[date][timestamp]['keff'][...]
			num_angles = f[date][timestamp]['# azimuthal angles'][...]
			all_kinf[num_angles/4-1] = calculated_kinf
			all_azim[num_angles/4-1] = num_angles
	f.close()

	#finds kinf from casmo
	directory = 'studies/' + assembly + '/casmo-reference/'
	filename = directory + 'casmo-data.h5'
	f = h5py.File(filename)
	actual_kinf = f['Casmo Data']['K-Infinity'][...]
	f.close()

	#calculates kinf error
	kinf_error = numpy.zeros((num_cases))
	for i in range(num_cases): 
		kinf_error[i] = ((all_kinf[i] - actual_kinf)*1e5)

	#plots kinf
	fig = plt.figure()
	plt.plot(all_azim, kinf_error)
	plt.xlabel('# Azimuthal Angles')
	plt.ylabel('Error [pcm]')
	plt.title ('Error in K-Infinity') 
	plt.legend(assemblies)
	plt.savefig('studies/'+assembly+'/kinf-error.png')
	
#to plot them all, make a big numpy array


#when plotting pin powers, plot max and mean vs angle
#account for 0 fission rate pins when calculating mean (take them out of average by dividing by less numbers)




