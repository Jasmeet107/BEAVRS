from openmoc import Lattice, universe_id
from pincells import pincells

# create dictionary of lattices
lattices = dict()

pin_pitch = 1.25984
water_pitch = 1.25984
groups = ['2', '8']

for group in groups:
  lattices[group] = {}
  
  ########################################################################### 
  ########################   Water Assembly   ###############################
  ###########################################################################

  w = pincells[group]['water'].getUniverseId()
  lattices[group]['water'] = Lattice(universe_id(), water_pitch, water_pitch)
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


  ########################################################################### 
  #################   1.6 % enriched w/o BP Assembly   ######################
  ###########################################################################
  a = pincells[group]['pwru160c00']['uid']
  b = pincells[group]['pwru160c00']['guidetube']['uid']
  c = pincells[group]['pwru160c00']['instube']['uid']
  
  lattices[group]['1.6-0BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['1.6-0BP'].setLatticeCells([
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
      [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
      [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]])


  ########################################################################### 
  #################   2.4 % enriched w/o BP Assembly   ######################
  ###########################################################################
  a = pincells[group]['pwru240c00']['uid']
  b = pincells[group]['pwru240c00']['guidetube']['uid']
  c = pincells[group]['pwru240c00']['instube']['uid']
  
  lattices[group]['2.4-0BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['2.4-0BP'].setLatticeCells([
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
      [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
      [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]])


  ########################################################################### 
  #################   3.1 % enriched w/o BP Assembly   ######################
  ###########################################################################  
  a = pincells[group]['pwru310c00']['uid']
  b = pincells[group]['pwru310c00']['guidetube']['uid']
  c = pincells[group]['pwru310c00']['instube']['uid']

  lattices[group]['3.1-0BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-0BP'].setLatticeCells([
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
      [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
      [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]])
  

  ########################################################################### 
  #################   3.1 % enriched w/ 6 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru310w06']['uid']
  b = pincells[group]['pwru310w06']['guidetube']['uid']
  c = pincells[group]['pwru310w06']['instube']['uid']
  d = pincells[group]['pwru310w06']['bp']['uid']
  
  lattices[group]['3.1-6tBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-6lBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-6rBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-6bBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)

  configT = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, d, a, a, b, a, a, d, a, a, a, a, a],
             [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a] ,
             [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  # rotate counterclockwise
  configL = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, d, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, d, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, d, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, d, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  configR = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, b, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
             [a, a, a, a, a, d, a, a, b, a, a, d, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  configB = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, d, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, d, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, d, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, d, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  lattices[group]['3.1-6tBP'].setLatticeCells(configT)
  lattices[group]['3.1-6lBP'].setLatticeCells(configL)
  lattices[group]['3.1-6rBP'].setLatticeCells(configR)
  lattices[group]['3.1-6bBP'].setLatticeCells(configB)


  ########################################################################### 
  ################   2.4 % enriched w/ 12 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru240w12']['uid']
  b = pincells[group]['pwru240w12']['guidetube']['uid']
  c = pincells[group]['pwru240w12']['instube']['uid']
  d = pincells[group]['pwru240w12']['bp']['uid']

  lattices[group]['2.4-12BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)

  cycle1 = [
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, d, a, a, b, a, a, d, a, a, a, a, a],
    [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
    [a, a, a, a, a, d, a, a, b, a, a, d, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  lattices[group]['2.4-12BP'].setLatticeCells(cycle1)


  ########################################################################### 
  ################   3.1 % enriched w/ 12 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru310w12']['uid']
  b = pincells[group]['pwru310w12']['guidetube']['uid']
  c = pincells[group]['pwru310w12']['instube']['uid']
  d = pincells[group]['pwru310w12']['bp']['uid']

  lattices[group]['3.1-12BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)

  cycle1 = [
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, d, a, a, b, a, a, d, a, a, a, a, a],
    [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, b, a, a, b, a, a, c, a, a, b, a, a, b, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
    [a, a, a, a, a, d, a, a, b, a, a, d, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
    [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]
  
  lattices[group]['3.1-12BP'].setLatticeCells(cycle1)


  ########################################################################### 
  ################   3.1 % enriched w/ 15 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru310w15']['uid']
  b = pincells[group]['pwru310w15']['guidetube']['uid']
  c = pincells[group]['pwru310w15']['instube']['uid']
  d = pincells[group]['pwru310w15']['bp']['uid']

  lattices[group]['3.1-15tBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-15lBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-15rBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-15bBP'] = Lattice(universe_id(), pin_pitch, pin_pitch)

  configT = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
             [a, a, a, d, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, d, a, a, d, a, a, d, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, d, a, a, c, a, a, d, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, d, a, a, d, a, a, d, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  configL = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, d, a, a, d, a, a, d, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, d, a, a, c, a, a, d, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, d, a, a, d, a, a, d, a, a, d, a, a, b, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, d, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  configR = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, d, a, a, d, a, a, d, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, d, a, a, c, a, a, d, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, d, a, a, d, a, a, d, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, d, a, a, a],
             [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]

  configB = [[a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, d, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, d, a, a, d, a, a, d, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, d, a, a, c, a, a, d, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, b, a, a, d, a, a, d, a, a, d, a, a, d, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, b, a, a, a, a, a, a, a, a, a, b, a, a, a],
             [a, a, a, a, a, b, a, a, b, a, a, b, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
             [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]]
  
  lattices[group]['3.1-15tBP'].setLatticeCells(configT)
  lattices[group]['3.1-15lBP'].setLatticeCells(configL)
  lattices[group]['3.1-15rBP'].setLatticeCells(configR)
  lattices[group]['3.1-15bBP'].setLatticeCells(configB)


  ########################################################################### 
  ################   2.4 % enriched w/ 16 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru240w16']['uid']
  b = pincells[group]['pwru240w16']['guidetube']['uid']
  c = pincells[group]['pwru240w16']['instube']['uid']
  d = pincells[group]['pwru240w16']['bp']['uid']

  lattices[group]['2.4-16BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['2.4-16BP'].setLatticeCells([
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
      [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, c, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
      [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]])
  

  ########################################################################### 
  ################   3.1 % enriched w/ 16 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru310w16']['uid']
  b = pincells[group]['pwru310w16']['guidetube']['uid']
  c = pincells[group]['pwru310w16']['instube']['uid']
  d = pincells[group]['pwru310w16']['bp']['uid']

  lattices[group]['3.1-16BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-16BP'].setLatticeCells([
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
      [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, c, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, b, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
      [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]])
  

  ########################################################################### 
  ################   3.1 % enriched w/ 20 BP Assembly   #####################
  ###########################################################################  
  a = pincells[group]['pwru310w20']['uid']
  b = pincells[group]['pwru310w20']['guidetube']['uid']
  c = pincells[group]['pwru310w20']['instube']['uid']
  d = pincells[group]['pwru310w20']['bp']['uid']

  lattices[group]['3.1-20BP'] = Lattice(universe_id(), pin_pitch, pin_pitch)
  lattices[group]['3.1-20BP'].setLatticeCells([
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
      [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, d, a, a, b, a, a, d, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, b, a, a, c, a, a, b, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, d, a, a, d, a, a, b, a, a, d, a, a, d, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, d, a, a, a, a, a, a, a, a, a, d, a, a, a],
      [a, a, a, a, a, d, a, a, d, a, a, d, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
      [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a]])
  
