from openmoc import * 
from openmoc.compatible.casmo import *
import openmoc.plotter as plotter
import openmoc.log as log
import h5py
import numpy
import matplotlib.pyplot as plt
from beavrs2d import *
from beavrs2d.generatehdf5 import generate_some


def importxsFromCasmo(name, group): 
	generate_some(name, group)
	
def computeKinfError():

	#finds kinf from simulation for all cases
	f = h5py.File('simulation-states/simulation-state.h5', 'r')
	all_kinf = numpy.zeros((31))
	dates = f.keys()
	for date in dates: 
		timestamps = f[date].keys()
			for timestamp in timestamps: 
				calculated_kinf = f[timestamp]['keff'][...]
				num_angles = f[timestamp]['# azimuthal angles']
				all_kinf[num_angles/4-1] = calculated_kinf
	f.close()
	
	#finds kinf from casmo
	f = h5py.File('casmo-reference/casmo-data.h5')
	actual_kinf = f['Casmo Data']['K-Infinity']
	f.close()

	kinf_error = numpy.zeros((31))
	for i in enumerate(all_kinf): 
		kinf_error[i] = abs((all_kinf[i] - actual_kinf)/(actual_kinf))

	return kinf_error
	
	
def plotter(X, Y, title, x_name, y_name, x_scale, y_scale, filename, num_datasets, legend = []):
	fig = plt.figure()
	colors = ['b', 'g', 'r', 'k', 'm']
	for i in range(num_datasets):
		plt.plot(X[i], Y[i], colors[i] + 'o-', ms = 10, lw = 2)
	if x_name == 'Track Spacing':
		plt.axis([x_scale, 0, 0, y_scale])
	else:
		plt.axis([0, x_scale, 0, y_scale])
	plt.title(title)
	plt.xlabel(x_name)
	plt.ylabel(y_name)
	plt.grid()
	if num_datasets > 1:
		plt.legend(legend)
	plt.show()
	fig.savefig(filename)
	



'''def computePinPowerError(solver, pin_directory, assembly_name):

    #finds pin powers from simulation FOR ALL CASES
    f = h5py.File('simulation-state/simulation-state.h5', 'r')
    allPinPowers = numpy.zeros((number of cases, width of assembly, length of assembly)) 
    timestamps = f.keys() #something like this
    for timestamp in timestamps: 
    	#cpp is an array
    	calculatedPinPowers = f[timestamp]['fission-rates'][...] #also something like this, use HDFView to find indices
    	normalizedPinPowers = calculatedPinPowers/numpy.sum(calculatedPinPowers)
    	numAngles = f[timestamp]['numangles'] #something like this
    	allPinPowers[numAngles/4-1, :, :] = normalizedPinPowers
    f.close()

    #finds pin powers from casmo #will only have one "case" because it's the true array
    f = h5py.File(pin_directory + assembly_name + '-results.hdf5')
    actualPinPowers = f['Pin Powers'][...]
    f.close()
    normalized_actualPinPowers = actualPinPowers/numpy.sum(actualPinPowers)


    #finds pinError : go through each case and compute error between that case and casmo values
    #for array in allpinpowers:
    pinError = numpy.zeros(normalized_actualPinPowers.shape)
    for i in range(normalized_actualPinPowers.shape[0]):
        for j in range(normalized_actualPinPowers.shape[1]):
            if normalized_actualPinPowers[i][j] != 0:
                pinError[i][j] = (normalizedPinPowers[i][j] - normalized_actualPinPowers[i][j]) / normalized_actualPinPowers[i][j]
            elif normalized_actualPinPowers[i][j] == 0:
                pinError[i][j] = 0
    max_error = numpy.max(abs(pinError))
    pinError_sum = 0
    numErrors = 0
    for i in range(pinError.shape[0]):
        for j in range(pinError.shape[1]):
            pinError_sum += abs(pinError[i][j])
            if pinError[i][j] != 0:
                numErrors += 1
    mean_error = pinError_sum / numErrors
    
    return max_error, mean_error, calculatedPinPowers


def computeKinfError(solver, pin_directory, assembly_name):

    #finds kinf from simulation
    calculated_kinf = solver.getKeff()
    #finds kinf from casmo
    f = h5py.File(pin_directory + assembly_name + '-results.hdf5')
    actual_kinf = f.attrs['K-Infinity']
    f.close()

    kinf_error = abs((calculated_kinf - actual_kinf)/(actual_kinf))

    return kinf_error

def storeError(assembly_name, study_name, max_errors, mean_errors, kinf_errors):
    
    f = h5py.File('results/' + assembly_name + '-errors.h5')
    f.attrs['Energy Groups'] = 2
    current_test = f.require_group(study_name)
    keys = max_errors.keys()
    for key in keys:
        current_test.require_dataset('%s_max_%s' % (study_name, key), (), '=f8', exact=False, data=max_errors[key])
        current_test.require_dataset('%s_mean_%s' % (study_name, key), (), '=f8', exact=False, data=mean_errors[key])
        current_test.require_dataset('%s_kinf_%s' % (study_name, key), (), '=f8', exact=False, data=kinf_errors[key])
    f.close()

def plotter(X, Y, title, x_name, y_name, x_scale, y_scale, filename, num_datasets, legend = []):
    fig = plt.figure()
    colors = ['b', 'g', 'r', 'k', 'm']
    for i in range(num_datasets):
        plt.plot(X[i], Y[i], colors[i] + 'o-', ms = 10, lw = 2)
    if x_name == 'Track Spacing':
        plt.axis([x_scale, 0, 0, y_scale])
    else:
        plt.axis([0, x_scale, 0, y_scale])
    plt.title(title)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.grid()
    if num_datasets > 1:
        plt.legend(legend)
    plt.show()
    fig.savefig(filename)

def pinPowerPlotter(pin_directory):

    f = h5py.File('pin-powers/fission-rates.h5', 'r')
    calculatedPinPowers = f['universe0']['fission-rates'][...]
    normalizedPinPowers = calculatedPinPowers/numpy.sum(calculatedPinPowers)
    f.close()

    plt.figure()
    plt.pcolor(numpy.linspace(0, 17, 17), numpy.linspace(0, 17, 17), normalizedPinPowers, edgecolors = 'k', linewidths = 1, vmin = normalizedPinPowers[:,:].min(), vmax = normalizedPinPowers[:,:].max())
    plt.colorbar()
    plt.axis([0,17,0,17])
    plt.title('Normalized Pin Powers')
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    plt.show()'''
