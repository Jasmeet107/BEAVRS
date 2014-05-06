from openmoc import Lattice, universe_id
from pincells import pincells

lattices = dict() #creates dictionary of lattices
pinPitch = 1.25984


################################################################################
#############################  0 Burnable Poisons ##############################
################################################################################

a = pincells['16fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['1.6-0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['1.6-0BP'].setLatticeCells([
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

a = pincells['24fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['2.4-0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['2.4-0BP'].setLatticeCells([
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

a = pincells['31fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['3.1-0BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-0BP'].setLatticeCells([
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
a = pincells['31fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['3.1-6tBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-6lBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-6rBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-6bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

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

lattices['3.1-6tBP'].setLatticeCells(configT)
lattices['3.1-6lBP'].setLatticeCells(configL)
lattices['3.1-6rBP'].setLatticeCells(configR)
lattices['3.1-6bBP'].setLatticeCells(configB)

################################################################################
#############################  12 Burnable Poisons #############################
################################################################################
a = pincells['24fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['2.4-12BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

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

lattices['2.4-12BP'].setLatticeCells(cycle1)

a = pincells['31fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['3.1-12BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

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

lattices['3.1-12BP'].setLatticeCells(cycle1)


################################################################################
#############################  *15 Burnable Poisons ##############################
################################################################################
a = pincells['31fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['3.1-15tBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-15lBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-15rBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-15bBP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)

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

lattices['3.1-15tBP'].setLatticeCells(configT)
lattices['3.1-15lBP'].setLatticeCells(configL)
lattices['3.1-15rBP'].setLatticeCells(configR)
lattices['3.1-15bBP'].setLatticeCells(configB)

################################################################################
#############################  16 Burnable Poisons ##############################
################################################################################
a = pincells['24fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['2.4-16BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['2.4-16BP'].setLatticeCells([
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

a = pincells['31fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['3.1-16BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-16BP'].setLatticeCells([
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
a = pincells['31fuel']['uid']
b = pincells['guidetube']['uid']
c = pincells['instube']['uid']
d = pincells['bp']['uid']

lattices['3.1-20BP'] = Lattice(id=universe_id(), width_x = pinPitch, width_y = pinPitch)
lattices['3.1-20BP'].setLatticeCells([
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
