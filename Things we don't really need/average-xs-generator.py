import h5py
import numpy
from casmo import *

def averageXSGenerator(self):
  xs_types = ['siga','sigd','sigt','sigf','signf','sigs']
  regions = ['fuel','water','cladding','helium','bp','zircaloy','ss304']
  variable_dict = {'siga':self._siga,'sigd':self._sigd,'sigt':self._sigt,'sigf':self._sigf,'signf':self._signf,'sigs':self._sigs}
  val_dict = {}
  for xs_type in xs_types:
    for region in regions:
      val_dict[xs_type][region] = []
  
  for i in range(len(self._cell_type_array)):
    for j in range(len(self._cell_type_array[i])):
      if string_pin_cell_array[i][j]=='gt':
        for xs_type in xs_types:
          val_dict[xs_type]['water'].append(variable_dict[xs_type][self._min_microregions[i][j])
          val_dict[xs_type]['cladding'].append(variable_dict[xs_type][self._min_microregions[i][j]+1)
          for k in range(self._min_microregions[i][j]+2,self.max_microregions[i][j]+1):
            val_dict[xs_type]['water'].append(variable_dict[xs_type][k])
      elif string_pin_cell_array[i][j]=='fuel':
        for xs_type in xs_types:
          val_dict[xs_type]['fuel'].append(variable_dict[xs_type][self._min_microregions[i][j])
          val_dict[xs_type]['helium'].append(variable_dict[xs_type][self._min_microregions[i][j]+1)
          val_dict[xs_type]['cladding'].append(variable_dict[xs_type][self._min_microregions[i][j]+2)
          for k in range(self._min_microregions[i][j]+3,self.max_microregions[i][j]+1):
            val_dict[xs_type]['water'].append(variable_dict[xs_type][k])
      elif string_pin_cell_array[i][j]=='bp':
        for xs_type in xs_types:
          val_dict[xs_type]['helium'].append(variable_dict[xs_type][self._min_microregions[i][j])
          val_dict[xs_type]['ss304'].append(variable_dict[xs_type][self._min_microregions[i][j]+1)
          val_dict[xs_type]['helium'].append(variable_dict[xs_type][self._min_microregions[i][j]+2)
          val_dict[xs_type]['bp'].append(variable_dict[xs_type][self._min_microregions[i][j]+3)
          val_dict[xs_type]['helium'].append(variable_dict[xs_type][self._min_microregions[i][j]+4)
          val_dict[xs_type]['ss304'].append(variable_dict[xs_type][self._min_microregions[i][j]+5)
          val_dict[xs_type]['water'].append(variable_dict[xs_type][self._min_microregions[i][j]+6)
          val_dict[xs_type]['zircaloy'].append(variable_dict[xs_type][self._min_microregions[i][j]+7)
          for k in range(self._min_microregions[i][j]+8,self.max_microregions[i][j]+1):
            val_dict[xs_type]['water'].append(variable_dict[xs_type][k])
      
  avg_dict = {}            
  for xs_type in xs_types:
    for region in regions:
      avg_dict[xs_type][region] = sum(val_dict[xs_type][region])/len(val_dict[xs_type][region])
