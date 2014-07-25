from openmoc import Lattice, universe_id
from pincells import pincells

lattices = dict() #creates dictionary of lattices
pinPitch = 1.25984
waterPitch = 1.25984
groups = ['2', '8']
for group in groups:
  lattices[group] = {}
  
  #Water Lattice
  w = pincells[group]['water'].getUniverseId()
  lattices[group]['water'] = Lattice(id=universe_id(), width_x = waterPitch, width_y = waterPitch)
  lattices[group]['water'].setLatticeCells([
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
  												[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]])


################################################################################
#############################  0 Burnable Poisons ##############################
################################################################################
  a = pincells[group]['pwru160c00']['uid']
  b = pincells[group]['pwru160c00']['guidetube']['uid']
  c = pincells[group]['pwru160c00']['instube']['uid']
  
  lattices[group]['1.6-0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['1.6-0BP'].setLatticeCells([
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

  a = pincells[group]['pwru240c00']['uid']
  b = pincells[group]['pwru240c00']['guidetube']['uid']
  c = pincells[group]['pwru240c00']['instube']['uid']
  
  lattices[group]['2.4-0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['2.4-0BP'].setLatticeCells([
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
  
  a = pincells[group]['pwru310c00']['uid']
  b = pincells[group]['pwru310c00']['guidetube']['uid']
  c = pincells[group]['pwru310c00']['instube']['uid']

  lattices[group]['3.1-0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-0BP'].setLatticeCells([
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
  #############################  *6 Burnable Poisons ##############################
  ################################################################################
  a = pincells[group]['pwru310w06']['uid']
  b = pincells[group]['pwru310w06']['guidetube']['uid']
  c = pincells[group]['pwru310w06']['instube']['uid']
  d = pincells[group]['pwru310w06']['bp']['uid']
  
  lattices[group]['3.1-6tBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-6lBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-6rBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-6bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

  configT = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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
  configL = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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
  configR = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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
  configB = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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

  lattices[group]['3.1-6tBP'].setLatticeCells(configT)
  lattices[group]['3.1-6lBP'].setLatticeCells(configL)
  lattices[group]['3.1-6rBP'].setLatticeCells(configR)
  lattices[group]['3.1-6bBP'].setLatticeCells(configB)

  ################################################################################
  #############################  12 Burnable Poisons #############################
  ################################################################################
  a = pincells[group]['pwru240w12']['uid']
  b = pincells[group]['pwru240w12']['guidetube']['uid']
  c = pincells[group]['pwru240w12']['instube']['uid']
  d = pincells[group]['pwru240w12']['bp']['uid']

  lattices[group]['2.4-12BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

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

  lattices[group]['2.4-12BP'].setLatticeCells(cycle1)

  a = pincells[group]['pwru310w12']['uid']
  b = pincells[group]['pwru310w12']['guidetube']['uid']
  c = pincells[group]['pwru310w12']['instube']['uid']
  d = pincells[group]['pwru310w12']['bp']['uid']


  lattices[group]['3.1-12BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

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

  lattices[group]['3.1-12BP'].setLatticeCells(cycle1)


  ################################################################################
  #############################  *15 Burnable Poisons ##############################
  ################################################################################
  a = pincells[group]['pwru310w15']['uid']
  b = pincells[group]['pwru310w15']['guidetube']['uid']
  c = pincells[group]['pwru310w15']['instube']['uid']
  d = pincells[group]['pwru310w15']['bp']['uid']

  lattices[group]['3.1-15tBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-15lBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-15rBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-15bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

  configT = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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

  configL = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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
  configR = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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
  configB = [[a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a],
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

  lattices[group]['3.1-15tBP'].setLatticeCells(configT)
  lattices[group]['3.1-15lBP'].setLatticeCells(configL)
  lattices[group]['3.1-15rBP'].setLatticeCells(configR)
  lattices[group]['3.1-15bBP'].setLatticeCells(configB)

  ################################################################################
  #############################  16 Burnable Poisons ##############################
  ################################################################################
  a = pincells[group]['pwru240w16']['uid']
  b = pincells[group]['pwru240w16']['guidetube']['uid']
  c = pincells[group]['pwru240w16']['instube']['uid']
  d = pincells[group]['pwru240w16']['bp']['uid']

  lattices[group]['2.4-16BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['2.4-16BP'].setLatticeCells([
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

  a = pincells[group]['pwru310w16']['uid']
  b = pincells[group]['pwru310w16']['guidetube']['uid']
  c = pincells[group]['pwru310w16']['instube']['uid']
  d = pincells[group]['pwru310w16']['bp']['uid']

  lattices[group]['3.1-16BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-16BP'].setLatticeCells([
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
  a = pincells[group]['pwru310w20']['uid']
  b = pincells[group]['pwru310w20']['guidetube']['uid']
  c = pincells[group]['pwru310w20']['instube']['uid']
  d = pincells[group]['pwru310w20']['bp']['uid']

  lattices[group]['3.1-20BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
  lattices[group]['3.1-20BP'].setLatticeCells([
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
