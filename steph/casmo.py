##
# @file casmo.py
# @package openmoc.compatible.casmo
# @brief The parsing module provides utility functions to parse in data 
#        necessary to construct assembly geometries in OpenMOC
# @author Davis Tran (dvtran@mit.edu)
# @date April 24, 2014

import numpy
import h5py
import os
import openmoc.log as log

##
# @class casmo.py "openmoc/compatible/casmo.py"
# @brief Contains data parsed from casmo output file
class Casmo(object):

  ##
  # @brief Casmo object class constructor
  def __init__(self):
    self._assembly_name = None
    self._filename = None
    self._directory = None
    self._energy_groups = None
    self._num_micro_regions = None
    self._siga = None
    self._sigd = None
    self._sigt = None
    self._sigf = None
    self._signf = None
    self._sigs = None
    self._chi = None
    self._width = None
    self._min_microregions = None
    self._max_microregions = None
    self._kinf = None
    self._pin_powers = None
    self._cell_types = {}
    self._cell_type_array = None 
    self._string_cell_type_array = None

  ##
  # @brief Returns assembly type as string
  # @param self the Casmo object pointer
  # @return assembly type (string)
  def getAssemblyname(self): 
    return self._assembly_name

  ##
  # @brief Sets assembly type
  # @param self the Casmo object pointer
  # @param assembly_name a string that indicates assembly type
  def setAssemblyName(self, assembly_name): 
    self._assembly_name = assembly_name

  ##
  # @brief Returns name of casmo output file to be parsed
  # @param self the Casmo object pointer
  # @return name of casmo output file to be parsed
  def getFileName(self): 
    return self._filename

  ##
  # @brief Sets file name of casmo output file to be parsed
  # @param self the Casmo object pointer
  # @param filename the name of the casmo output file to be parsed (string)
  def setFileName(self, filename): self._filename = filename

  ##
  # @brief Returns directory of casmo output file being parsed
  # @param self the Casmo object pointer
  # @return directory of casmo output file being parsed
  def getDirectory(self):
    return self._directory

  ##
  # @brief Sets directory of casmo output file to be parsed
  # @param self the Casmo object pointer
  # @param directory the directory of the casmo output file to be parsed (string)
  def setDirectory(self, directory): 
    self._directory = directory

  ##
  # @brief This method parses the casmo output file for the number of
  #        energy groups
  # @param self the Casmo object pointer
  # @return number of energy groups directly from casmo output file
  def parseEnergyGroups(self):
    f = open(self._directory + self._filename,'r')
    for line in f:
      if '[Usage Note]' in line:
        tokens = line.split()
        energy_groups = int(tokens[5])
        break
    f.close()
    return energy_groups
  
  ##
  # @brief Returns number of energy groups
  # @param self the Casmo object pointer
  # @return number of energy groups
  def getEnergyGroups(self): 
    return self._energy_groups

  ##
  # @brief Sets number of energy groups
  # @param self the Casmo object pointer
  # @param energy_groups number of energy groups (int)
  def setEnergyGroups(self, energy_groups):
    self._energy_groups = energy_groups

  ##
  # @brief parses and sets number of energy groups from casmo output file
  # @param self the Casmo object pointer
  def importEnergyGroups(self): 
    self.setEnergyGroups(self.parseEnergyGroups())

  ##
  # @brief This method parses the casmo output file for the number of 
  #        microregions in the assembly
  # @param self the Casmo object pointer
  # @return number of microregions directly from casmo output file
  def parseNumRegions(self):
    f = open(self._directory + self._filename, 'r')
    counter = 0
    for line in f:
      if "Micro-region" in line:
        counter += 1
        continue
      if counter == 1:
        tokens = line.split()
        num_micro_regions = int(tokens[1])
        break
    f.close()
    return num_micro_regions

  ##
  # @brief Returns number of microregions in assembly
  # @param self the Casmo object pointer
  # @return number of microregions
  def getNumRegions(self): 
    return self._num_micro_regions

  ##
  # @brief Sets the number of microregions
  # @param self the Casmo object pointer
  # @param num_micro_regions the number of microregions in the assembly
  def setNumRegions(self, num_micro_regions):
    self._num_micro_regions = num_micro_regions

  ##
  # @brief parses and sets number of microregions from casmo output file
  # @param self the Casmo object pointer
  def importNumRegions(self):
    self.setNumRegions(self.parseNumRegions())

  ##
  # @brief This method parses the casmo output file for the materials 
  #        cross sections for every microregion in the assembly
  # @param self the Casmo object pointer
  # @param xs_name the name of cross section type (string in all CAPS)
  # @return numpy array of cross sections
  def parseXS(self, xs_name):

    # Parses for cross sections that are not the scattering matrix
    if xs_name != 'SIGS':
      xs_array = numpy.zeros((self._num_micro_regions, self._energy_groups))
      f = open(self._directory + self._filename, 'r')
      counter = 0
      for line in f:
        if xs_name in line:
          tokens = line.split()
          xs_array[counter, :] = [float(xs) for xs in tokens[2:2+self._energy_groups]]
          counter += 1
        if counter == self._num_micro_regions:
          break
      f.close()

    # Parses for scattering matrix cross sections
    if xs_name == 'SIGS':
      xs_array = numpy.zeros((self._num_micro_regions, self._energy_groups, self._energy_groups))
      f = open(self._directory + self._filename, "r")
      cur_region = 0
      cur_group = 0
      for line in f:
        if xs_name in line:
          words = line.split()
          xs_array[cur_region, cur_group, :] = [float(xs) for xs in words[2:2+self._energy_groups]]
          cur_group += 1
        if cur_group == self._energy_groups:
          cur_region += 1
          cur_group = 0
        if cur_region == self._num_micro_regions:
          break
    f.close()
    return xs_array

  ##
  # @brief Returns a specific cross section numpy array
  # @param self the Casmo object pointer
  # @param xs_name the name of a type of cross section (string)
  # @return a cross section numpy array
  def getXS(self, xs_name):
    '''Retrieves cross-section attribute.'''

    if xs_name == 'SIGA':
      return self._siga
    if xs_name == 'SIGD':
      return self._sigd
    if xs_name == 'SIGT':
      return self._sigt
    if xs_name == 'SIGF':
      return self._sigf
    if xs_name == 'SIGNF':
      return self._signf
    if xs_name == 'SIGS':
      return self._sigs
    if xs_name == 'CHI':
      return self._chi

  ##
  # @brief Sets a specific cross section
  # @param self the Casmo object pointer
  # @param xs_name the name of a type of cross section (string)
  # @param xs_array a numpy array of cross section values
  def setXS(self, xs_name, xs_array):

    if xs_name == 'SIGA':
      self._siga = xs_array
    if xs_name == 'SIGD':
      self._sigd = xs_array
    if xs_name == 'SIGT':
      self._sigt = xs_array
    if xs_name == 'SIGF':
      self._sigf = xs_array
    if xs_name == 'SIGNF':
      self._signf = xs_array
    if xs_name == 'SIGS':
      self._sigs = xs_array
    if xs_name == 'CHI':
      self._chi = xs_array

  ##
  # @brief parses and sets a specific cross section type from casmo ouput file
  # @param self the Casmo object pointer
  # @param xs_name the name of a type of cross section (string)
  def importXS(self, xs_name):
    self.setXS(xs_name, self.parseXS(xs_name))

  ##
  # @brief calls importXS for all types of cross sections needed by OpenMOC
  # @param self the Casmo object pointer
  def importAllXS(self):
    xs_list = ['SIGA', 'SIGD', 'SIGT', 'SIGF', 'SIGNF', 'SIGS', 'CHI']
    for xs_name in xs_list:
      self.importXS(xs_name)

  ##
  # @brief This method parses the casmo output file for the dimensions of
  #        the assembly. The width equals the number of fuel pins in a row
  #        or column of an assembly.
  # @param self the Casmo object pointer
  # @return width of the assembly
  def parseWidth(self):

    half_width = -1
    f = open(self._directory + self._filename, "r")
    for line in f:
      if "Layout" in line:
        half_width += 1
        continue
      if half_width>=0 and line == '\n':
        break
      if half_width>=0:
        half_width += 1
    f.close()
    return half_width*2-1

  ##
  # @brief Returns width of the assembly
  # @param self the Casmo object pointer
  # @return width of the assembly (int)
  def getWidth(self):
    return self._width = width

  ##
  # @brief Sets width of the assembly
  # @param self the Casmo object pointer
  # @param width the width to be set for the assembly
  def setWidth(self, width):
    self._width = width

  ##
  # @brief parses and sets a width of assembly from casmo ouput file
  # @param self the Casmo object pointer
  def importWidth(self):
    self.setWidth(self.parseWidth())

  ##
  # @brief This method parses the casmo output file for microregion ranges
  #        and returns a tuple of two numpy arrays, one is the minimum values
  #        and the other is the maximum values of those microregion ranges, each
  #        each located within its specific macroregion
  # @param self the Casmo object pointer
  # @return numpy array tuple (min microregion values, max microregion values)
  def parseMicroregions(self):

    half_width = (self._width+1)/2
    min_array = numpy.zeros((self._width,self._width), dtype=numpy.int32)
    max_array = numpy.zeros((self._width,self._width), dtype=numpy.int32)
    min_quadrant4 = numpy.zeros((half_width,half_width), dtype=numpy.int32)
    max_quadrant4 = numpy.zeros((half_width,half_width), dtype=numpy.int32)

    f = open(self._directory + self._filename, 'r')
    counter = 0
    for line in f:
      if counter >= 1 and "1_________" in line:
        break
      if "Micro-region" in line:
        counter += 1
        continue
      if counter >= 1:
        tokens = line.split()
        for index, token in enumerate(tokens):
          token = token.strip("*")
          token = token.strip("-")
          if index%2 ==0:
            min_quadrant4[counter-1, index/2] = float(token)
            min_quadrant4[index/2, counter-1] = float(token)
          else:
            max_quadrant4[counter-1, (index-1)/2] = float(token)
            max_quadrant4[(index-1)/2, counter-1] = float(token)
        counter += 1
    f.close()

    min_array[(half_width-1):,(half_width-1):] = min_quadrant4
    min_array[(half_width-1):, 0:(half_width)] = numpy.fliplr(min_quadrant4)
    min_array[0:(half_width), (half_width-1):] = numpy.flipud(min_quadrant4)
    min_array[0:(half_width), 0:(half_width)] = numpy.flipud(numpy.fliplr(min_quadrant4))

    max_array[(half_width-1):,(half_width-1):] = max_quadrant4
    max_array[(half_width-1):, 0:(half_width)] = numpy.fliplr(max_quadrant4)
    max_array[0:(half_width), (half_width-1):] = numpy.flipud(max_quadrant4)
    max_array[0:(half_width), 0:(half_width)] = numpy.flipud(numpy.fliplr(max_quadrant4))

    return min_array, max_array

  ##
  # @brief Returns numpy array of minimum values of microregion range within
  #        each macroregion
  # @param self the Casmo object pointer
  # @return numpy array of minimum values of microregion ranges
  def getMinMicroregions(self):
    return self._min_microregions

  ##
  # @brief Sets minimum values of microregion ranges within each macroregion
  # @param self the Casmo object pointer
  # @param min_array numpy array of minimum values of microregion ranges
  def setMinMicroregions(self, min_array):
    self._min_microregions = min_array

  ##
  # @brief Returns numpy array of maximum values of microregion ranges within
  #        each macroregion
  # @param self the Casmo object pointer
  # @return numpy array of maximum values of microregion ranges
  def getMaxMicroregions(self):
    return self._max_microregions

  ##
  # @brief Sets minimum values of microregion ranges within each macroregion
  # @param self the Casmo object pointer
  # @param max_array numpy array of minimum values of microregion ranges
  def setMaxMicroregions(self, max_array):
    self._max_microregions = max_array

  ##
  # @brief parses and sets microregion value numpy arrays
  # @param self the Casmo object pointer
  def importMicroregions(self):
      self.setMinMicroregions(self.parseMicroregions()[0])
      self.setMinMicroregions(self.parseMicroregions()[1])

  ##
  # @brief This method parses the casmo output file for reference eigenvalue
  # @param self the Casmo object pointer
  # @return reference eigenvalue of assembly (float)
  def parseKinf(self):
    f = open(self._directory + self._filename, 'r')

    for line in f:
        if "k-infinity" in line:
            tokens = line.split()
            kinf = float(tokens[2])
            break
    f.close()
    return kinf

  ##
  # @brief Returns reference eigenvalue of assembly from casmo output file
  # @param self the Casmo object pointer
  # @return reference eigenvalue of assembly (float)
  def getKinf(self):
    return self._kinf

  ##
  # @brief Sets reference eigenvalue of assembly
  # @param self the Casmo object pointer
  # @param kinf the reference eigenvalue to be set for the assembly
  def setKinf(self, kinf):
    self._kinf = kinf

  ##
  # @brief parses and sets eigenvalue of assembly
  # @param self the Casmo object pointer
  def importKinf(self):
    self.setKinf(self.parseKinf())

  ##
  # @brief This method parses the casmo output file for reference pin powers
  # @param self the Casmo object pointer
  # @return numpy array of float-valued reference pin powers of assembly
  def parseRings

  ##
  # @brief This method parses the casmo output file for reference pin powers
  # @param self the Casmo object pointer
  # @return numpy array of float-valued reference pin powers of assembly
  def parsePinPowers(self):

    f = open(self._directory + self._filename, 'r')

    half_width = (self._width+1)/2
    pin_power_array = numpy.zeros((self._width,self._width), dtype=numpy.float32)
    quadrant4 = numpy.zeros((half_width,half_width), dtype=numpy.float32)

    counter = 0
    for line in f:
      if counter >= 1 and line == "\n":
        break
      if "Power Distribution" in line:
        counter += 1
        continue
      if counter >= 1:
        powers = line.split()
        for index, power in enumerate(powers):
          power = power.strip("*")
          quadrant4[counter-1, index] = float(power)
          quadrant4[index, counter-1] = float(power)
        counter += 1
    f.close()
    
    # Arranges section of pin powers into larger array by symmetry
    pin_power_array[(half_width-1):,(half_width-1):] = quadrant4
    pin_power_array[(half_width-1):, 0:(half_width)] = numpy.fliplr(quadrant4)
    pin_power_array[0:(half_width), (half_width-1):] = numpy.flipud(quadrant4)
    pin_power_array[0:(half_width), 0:(half_width)] = numpy.flipud(numpy.fliplr(quadrant4))

    return pin_power_array

  ##
  # @brief Returns reference pin powers of assembly from casmo output file
  # @param self the Casmo object pointer
  # @return numpy array of float valued reference pin powers of assembly
  def getPinPowers(self):
    return self._pin_powers

  ##
  # @brief Sets reference pin powers of assembly
  # @param self the Casmo object pointer
  # @param pin_power_array numpy array of float-valued reference pin powers
  def setPinPowers(self, pin_power_array):
    self._pin_powers = pin_power_array

  ##
  # @brief parses and sets pin powers of assembly
  # @param self the Casmo object pointer
  def importPinPowers(self):
    self.setPinPowers(self.parsePinPowers())

  ##
  # @brief Returns dictionary of cell type associated with each id number
  # @param self the Casmo object pointer
  # @return dictionary cell types by id number, int-->string
  def getCellTypes(self):
    return self._cell_types

  ##
  # @brief Sets a cell type and cell type id key-value pair
  # @param self the Casmo object pointer
  # @param cell_types_id id number for a certain cell type (int)
  # @param name name of a specific cell type associated an id number (string)
  def setCellType(self, cell_types_id, name):
    self._cell_types[cell_types_id] = name

  ##
  # @brief This method parses the casmo output file for the type of material in
  #        each cell
  # @param self the Casmo object pointer
  # @return numpy array of int-valued cell types
  def parseCellTypeArray(self):

    half_width = (self._width+1)/2
    full_width = self._width
    cell_type_array = numpy.zeros((full_width,full_width), dtype=numpy.int32)
    quadrant4 = numpy.zeros((half_width,half_width), dtype=numpy.int32)

    counter = 0
    f = open(self._directory + self._filename, 'r')
    for line in f:
      if counter >=1 and line == '\n':
        break
      if 'Layout' in line:
        counter += 1
        continue
      if counter >= 1:
        cell_types = line.split()
        for index, cell_type in enumerate(cell_types):
          cell_type = cell_type.strip('*')
          quadrant4[counter-1, index] = int(cell_type)
        counter += 1
    f.close()
    
    # Arranges section of cell types into larger array by symmetry
    cell_type_array[(half_width-1):,(half_width-1):] = quadrant4
    cell_type_array[(half_width-1):, 0:(half_width)] = numpy.fliplr(quadrant4)
    cell_type_array[0:(half_width), (half_width-1):] = numpy.flipud(quadrant4)
    cell_type_array[0:(half_width), 0:(half_width)] = numpy.flipud(numpy.fliplr(quadrant4))

    cell_type_array[half_width-1,half_width-1] = 2
	
    return cell_type_array

  ##
  # @brief Returns array of cell type ids for assembly
  # @param self the Casmo object pointer
  # @return array of cell types for every cell in assembly
  def getCellTypeArray(self):
    return self._cell_type_array

  ##
  # @brief Sets array of cell type ids for assembly
  # @param self the Casmo object pointer
  # @param cell_type_array numpy array of int-valued cell type ids
  def setCellTypeArray(self, cell_type_array):
    self._cell_type_array = cell_type_array

  ##
  # @brief parses and sets cell type ids for assembly
  # @param self the Casmo object pointer
  def importCellTypeArray(self):
    self.setCellTypeArray(self.parseCellTypeArray())

  ##
  # @brief This method converts the numerical cell type array to strings that
  #        indicate the cell type in clearer language
  # @param self the Casmo object pointer
  # @return numpy array of cell types as strings
  def stringCellTypeArray(self):

    #id of 1 corresponds to fuel (string of fuel)
    #id of 2 corresponds to guide tube (string of gt)
    #id of 3 corresponds to burnable poison (string of bp)
    string_cell_type_array = numpy.zeros((self._width,self._width), dtype=numpy.str)


    for i, row in enumerate(self._cell_type_array):
      for j, cell in enumerate(row):
        if self._cell_type_array[i,j] in self._cell_types.keys():
          string_cell_type_array[i,j] = self._cell_types[self._cell_type_array[i,j]]
        else:
          log.py_printf('WARNING', 'Cell type id %d does not exist. Call setCellTypes to set cell name for id.', cell_type_array[i,j])

    return string_cell_type_array
    '''
    for i, row in enumerate(cell_type_array):
      for j, cell in enumerate(row):
        if cell_type_array[i,j] == 1:
          string_cell_type_array[i,j] = 'fuel'
        elif cell_type_array[i,j] == 2:
          string_cell_type_array[i,j] = 'gt'
        elif cell_type_array[i,j] == 3:
          string_cell_type_array[i,j] = 'bp'
    '''

  ##
  # @brief Returns array of cell types as strings for assembly
  # @param self the Casmo object pointer
  # @return array of cell types as strings for assembly
  def getStringCellTypeArray(self):
    return self._string_cell_type_array

  ##
  # @brief Sets array of cell types as strings for assembly
  # @param self the Casmo object pointer
  # @param string_cell_type_array array of cell types as strings
  def setStringCellTypeArray(self, string_cell_type_array):
    self._string_cell_type_array = string_cell_type_array

  ##
  # @brief This method calls the Casmo import methods necessary to construct
  #        the geometry of an assembly in OpenMOC
  # @param self the Casmo object pointer
  # @param filename filename of casmo output file to be parsed
  # @param directory directory of casmo output file to be parsed
  def importFromCASMO(self, filename, directory):
    self._filename = filename
    self._directory = directory
    self.importEnergyGroups()
    self.importNumRegions()
    self.importAllXS()
    self.importWidth()
    self.importMicroregions()
    self.importKinf()
    self.importPinPowers()
    self.importCellTypeArray()

  ##
  # @brief This method exports all data contained within member variables
  #        of the Casmo object to an hdf5 data file, data sets expect arrays
  # @param self the Casmo object pointer
  # @param filename filename of hdf5 data file
  # @param directory directory where hdf5 data file will be stored
  def export(self, directory = 'casmo-data/', filename = 'casmo-data.h5'):
    f = h5py.File(directory + filename)
    f.attrs['Energy Groups'] = self._energy_groups
    f.attrs['K-Infinity'] = self._kinf
    sigma_t = f.create_group('Total XS')
    sigma_t.create_dataset('Total XS', data=self._sigt)
    sigma_a = f.create_group('Absorption XS')
    sigma_a.create_dataset('Absorption XS', data=self._siga)
    sigma_f = f.create_group('Fission XS')
    sigma_f.create_dataset('Fission XS', data=self._sigf)
    sigma_nf = f.create_group('Nu Fission XS')
    sigma_nf.create_dataset('Nu Fission XS', data=self._signf)
    sigma_s = f.create_group('Scattering XS')
    sigma_s.create_dataset('Scattering XS', data=self._sigs)
    sigma_d = f.create_group('Dif Coefficient')
    sigma_d.create_dataset('Dif Coefficient', data=self._sigd)
    chi = f.create_group('Chi')
    chi.create_dataset('Chi', data=self._chi)
    pin_powers = f.create_group('Pin Powers')
    pin_powers.create_dataset('Pin Powers', data=self._pin_powers)
    cell_types = f.create_group('Cell Types')
    cell_types.create_dataset('Cell Types', data=self._cell_type_array)
    min_microregions = f.create_group('Min Microregions')
    min_microregions.create_dataset('Min Microregions', data=self._min_microregions)
    max_microregions = f.create_group('Max Microregions')
    max_microregions.create_dataset('Max Microregions', data=self._max_microregions)
    f.close()

  ##
  # @brief This method imports data from an hdf5 data file and assigns it
  #        to the corresponding member variables
  # @param self the Casmo object pointer
  # @param filename filename of hdf5 data file
  # @param directory directory where hdf5 data file is stored
  def importFromHDF5(self, directory = 'casmo-data/', filename = 'casmo-data.h5'):
    f = h5py.File(directory + filename, 'r')
    self._directory = directory    
    self._filename = filename
    self._energy_groups = f['Energy Groups']
    self._kinf = f['K-Infinity']
    self._sigt = f['Total XS'][...]
    self._siga = f['Absorption XS'][...]
    self._sigf = f['Fission XS'][...]
    self._signf = f['Nu Fission XS'][...]
    self._sigs = f['Scattering XS'][...]
    self._sigd = f['Dif Coefficient'][...]
    self._chi = f['Chi'][...]
    self._pin_powers = f['Pin Powers'][...]
    self._cell_type_array = f['Cell Types'][...]
    self._min_microregions = f['Min Microregions'][...]
    self._max_microregions = f['Max Microregions'][...]
    self._width = self._max_microregions.shape[0]
    self._num_micro_regions = self._sigt.shape[0]
    f.close()

  ##
  # @brief This method exports only cross sectional arrays contained within 
  #        member variables of the Casmo object to an hdf5 data file
  # @param self the Casmo object pointer
  # @param assembly_name name of assembly for materials being exported
  # @param directory directory where hdf5 data file will be stored
  def xsToHDF5(self, assembly_name, directory = 'casmo-data'):

    os.system('rm ' + directory + '/' + assembly_name + '-materials.hdf5')
    if not os.path.exists(directory):
      os.makedirs(directory)


    f = h5py.File(directory + '/' + assembly_name + '-materials.hdf5')

    f.attrs['Energy Groups'] = self._energy_groups

    for region in range(self._num_micro_regions):
      material = f.create_group('microregion-' + str((region + 1)))
      material.create_dataset('Total XS', data=self._sigt[region, :])
      material.create_dataset('Absorption XS', data=self._siga[region, :])
      material.create_dataset('Fission XS', data=self._sigf[region, :])
      material.create_dataset('Nu Fission XS', data=self._signf[region, :])
      material.create_dataset('Scattering XS', data=numpy.ravel(self._sigs[region, :, :]))
      material.create_dataset('Dif Coefficient', data=self._sigd[region, :])
      material.create_dataset('Chi', data=self._chi[region, :])
    f.close()
