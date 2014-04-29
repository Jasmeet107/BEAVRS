from openmoc import Lattice, universe_id
import openmoc.plotter as plotter
from pincells import pincells

lattices = dict() #creates dictionary of lattices
pinPitch = 1.25984

for assemblyType in ['16fuel', '24fuel', '31fuel']: 

  lattices[assemblyType] = {}

  ################################################################################
  #############################  0 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['0BP'].setLatticeCells([
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
                      [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
                      [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]])

  ################################################################################
  #############################  4 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['4BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['4BP'].setLatticeCells([
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
                      [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                      [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]])

  ################################################################################
  #############################  *6 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['6aBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['6bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['6cBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['6dBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

  configA = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,d,a,a,b,a,a,d,a,a,a,a,a],
            [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]
  #rotate counterclockwise
  configB = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,d,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,d,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,d,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,d,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]
  configC = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,b,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
            [a,a,a,a,a,d,a,a,b,a,a,d,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]
  configD = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,d,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,d,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,d,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,d,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]

  lattices[assemblyType]['6aBP'].setLatticeCells(configA)
  lattices[assemblyType]['6bBP'].setLatticeCells(configB)
  lattices[assemblyType]['6cBP'].setLatticeCells(configC)
  lattices[assemblyType]['6dBP'].setLatticeCells(configD)



  ################################################################################
  #############################  8 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['8BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['8BP'].setLatticeCells([
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
                      [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,d,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,d,a,a,c,a,a,d,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,b,a,a,b,a,a,d,a,a,b,a,a,b,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                      [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                      [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]])

  ################################################################################
  #############################  *12 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['12aBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['12bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

  cycle2=[
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,d,a,a,b,a,a,d,a,a,a,a,a],
         [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,d,a,a,b,a,a,d,a,a,b,a,a,d,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,b,a,a,d,a,a,c,a,a,d,a,a,b,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,d,a,a,b,a,a,d,a,a,b,a,a,d,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
         [a,a,a,a,a,d,a,a,b,a,a,d,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]

  cycle1 = [
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,d,a,a,b,a,a,d,a,a,a,a,a],
         [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,d,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,b,a,a,b,a,a,c,a,a,b,a,a,b,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,d,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
         [a,a,a,a,a,d,a,a,b,a,a,d,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
         [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]

  lattices[assemblyType]['12aBP'].setLatticeCells(cycle1)
  lattices[assemblyType]['12bBP'].setLatticeCells(cycle2)

  ################################################################################
  #############################  *15 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['15aBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['15bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['15cBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['15dBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

  configA = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
            [a,a,a,d,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,d,a,a,d,a,a,d,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,d,a,a,c,a,a,d,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,d,a,a,d,a,a,d,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]

  configB = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,d,a,a,d,a,a,d,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,d,a,a,c,a,a,d,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,d,a,a,d,a,a,d,a,a,d,a,a,b,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,d,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]
  configC = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,d,a,a,d,a,a,d,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,d,a,a,c,a,a,d,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,d,a,a,d,a,a,d,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,d,a,a,a],
            [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]
  configC = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,d,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,d,a,a,d,a,a,d,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,d,a,a,c,a,a,d,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,b,a,a,d,a,a,d,a,a,d,a,a,d,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,b,a,a,a,a,a,a,a,a,a,b,a,a,a],
            [a,a,a,a,a,b,a,a,b,a,a,b,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
            [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]]

  lattices[assemblyType]['15aBP'].setLatticeCells(configA)
  lattices[assemblyType]['15bBP'].setLatticeCells(configB)
  lattices[assemblyType]['15cBP'].setLatticeCells(configC)
  lattices[assemblyType]['15dBP'].setLatticeCells(configD)

  ################################################################################
  #############################  16 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['16BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['16BP'].setLatticeCells([
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
                       [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,d,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,d,a,a,b,a,a,c,a,a,b,a,a,d,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,d,a,a,b,a,a,b,a,a,b,a,a,d,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                       [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]])

  ################################################################################
  #############################  20 Burnable Poisons ##############################
  ################################################################################
  a = pincells[assemblyType]['uid']
  b = pincells['guidetube']['uid']
  c = pincells['instube']['uid']
  d = pincells['bp']['uid']

  lattices[assemblyType]['20BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[assemblyType]['20BP'].setLatticeCells([
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
                       [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,d,a,a,d,a,a,b,a,a,d,a,a,d,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,d,a,a,b,a,a,c,a,a,b,a,a,d,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,d,a,a,d,a,a,b,a,a,d,a,a,d,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,d,a,a,a,a,a,a,a,a,a,d,a,a,a],
                       [a,a,a,a,a,d,a,a,d,a,a,d,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
                       [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]])
