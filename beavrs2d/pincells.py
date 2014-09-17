from openmoc import CellBasic, universe_id
from surfaces import surfaces
from materials import materials
from openmoc import *

# dictionary of pin cells
pincells = {} 
groups = ['2', '8']

for group in groups:
  pincells[group] = {}
	
  ##Creates Generic Water Cell
  pincells[group]['water'] = {}
  pincells[group]['water']['uid'] = universe_id() #sets universe ID for pin cell
  pincells[group]['water'] = CellBasic(universe=pincells[group]['water']['uid'], 
                                       material=materials[group]['pwru160c00']
                                       ['water'].getId())
  
  names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', \
                   'pwru310c00', 'pwru310w06', 'pwru310w12', \
                   'pwru310w15', 'pwru310w16', 'pwru310w20']
  
  for name in names: 
          
    ################################################################################
    #############################  Enriched Fuel Pins ##############################
    ################################################################################

    # dictionary of cells within this particular pin cell
    pincells[group][name] = {} 
    pincells[group][name]['uid'] = universe_id() #sets universe ID for pin cell
    
    # FUEL
    pincells[group][name]['fuel'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['fuel'].getId(), rings=3, sectors=8)
    pincells[group][name]['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

    # HELIUM
    pincells[group][name]['helium'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['helium'].getId(), sectors=8)
    pincells[group][name]['helium'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1'])
    pincells[group][name]['helium'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2'])
    
    # CLADDING
    pincells[group][name]['cladding'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['cladding'].getId(), sectors=8)
    pincells[group][name]['cladding'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2'])
    pincells[group][name]['cladding'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3'])
    
    # WATER
    pincells[group][name]['water'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['water'].getId(), sectors=8)
    pincells[group][name]['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-3'])
    
    
    ################################################################################
    ##########################  Guide Tube Pin Cells ###############################
    ################################################################################
    
    # dictionary of cells within this guide tube
    pincells[group][name]['guidetube'] = {}  
    pincells[group][name]['guidetube']['uid'] = universe_id()
    
    # WATER
    pincells[group][name]['guidetube']['water1'] = CellBasic(universe=pincells[group][name]['guidetube']['uid'], material=materials[group][name]['water'].getId(), rings=3, sectors=8)
    pincells[group][name]['guidetube']['water1'].addSurface(halfspace=-1, surface=surfaces['GT Radius-1'])
    
    # CLADDING
    pincells[group][name]['guidetube']['cladding'] = CellBasic(universe=pincells[group][name]['guidetube']['uid'], material=materials[group][name]['cladding'].getId(), sectors=8)
    pincells[group][name]['guidetube']['cladding'].addSurface(halfspace=+1, surface=surfaces['GT Radius-1'])
    pincells[group][name]['guidetube']['cladding'].addSurface(halfspace=-1, surface=surfaces['GT Radius-2'])
    
    # WATER
    pincells[group][name]['guidetube']['water2'] = CellBasic(universe=pincells[group][name]['guidetube']['uid'], material= materials[group][name]['water'].getId(), sectors=8)
    pincells[group][name]['guidetube']['water2'].addSurface(halfspace=+1, surface=surfaces['GT Radius-2'])
    
    
    
    ################################################################################
    #######################  Instrument Tube Pin Cells  ############################
    ################################################################################
    
    # dictionary of cells within this guide tube
    pincells[group][name]['instube'] = {} 
    pincells[group][name]['instube']['uid'] = universe_id()
    
    #AIR
    pincells[group][name]['instube']['helium'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material=materials[group][name]['helium'].getId(), rings=3, sectors=8)
    pincells[group][name]['instube']['helium'].addSurface(halfspace=-1, surface=surfaces['IT Radius-1'])
    
    # CLADDING
    pincells[group][name]['instube']['cladding1'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material=materials[group][name]['cladding'].getId(), sectors=8)
    pincells[group][name]['instube']['cladding1'].addSurface(halfspace=+1, surface=surfaces['IT Radius-1'])
    pincells[group][name]['instube']['cladding1'].addSurface(halfspace=-1, surface=surfaces['IT Radius-2'])
    
    # WATER
    pincells[group][name]['instube']['water1'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material=materials[group][name]['water'].getId(), sectors=8)
    pincells[group][name]['instube']['water1'].addSurface(halfspace=+1, surface=surfaces['IT Radius-2']) 
    pincells[group][name]['instube']['water1'].addSurface(halfspace=-1, surface=surfaces['IT Radius-3']) 
    
    # CLADDING
    pincells[group][name]['instube']['cladding2'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material=materials[group][name]['cladding'].getId(), sectors=8)
    pincells[group][name]['instube']['cladding2'].addSurface(halfspace=+1, surface=surfaces['IT Radius-3']) 
    pincells[group][name]['instube']['cladding2'].addSurface(halfspace=-1, surface=surfaces['IT Radius-4']) 
    
    # WATER
    pincells[group][name]['instube']['water2'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material= materials[group][name]['water'].getId(), sectors=8)
    pincells[group][name]['instube']['water2'].addSurface(halfspace=+1, surface=surfaces['IT Radius-4'])
    
    
  ################################################################################
  #######################  Burnable Absorber Pin Cell  ###########################
  ################################################################################
    
  names = ['pwru240w12', 'pwru240w16', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

  for name in names:
	
    # dictionary of cells within this guide tube
    pincells[group][name]['bp'] = {} 
    pincells[group][name]['bp']['uid'] = universe_id()
    
    # AIR
    pincells[group][name]['bp']['helium'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['helium'].getId(), rings=3, sectors=8)
    pincells[group][name]['bp']['helium'].addSurface(halfspace=-1, surface=surfaces['BP Radius-1'])
    
    # SS304
    pincells[group][name]['bp']['ss'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['ss304'].getId(), sectors=8)
    pincells[group][name]['bp']['ss'].addSurface(halfspace=+1, surface=surfaces['BP Radius-1'])
    pincells[group][name]['bp']['ss'].addSurface(halfspace=-1, surface=surfaces['BP Radius-2'])
    
    # AIR1
    pincells[group][name]['bp']['helium1'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['helium'].getId(), sectors=8)
    pincells[group][name]['bp']['helium1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-2'])
    pincells[group][name]['bp']['helium1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-3'])
    
    # BOROSILICATE GLASS
    pincells[group][name]['bp']['bg'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['bp'].getId(), sectors=8)
    pincells[group][name]['bp']['bg'].addSurface(halfspace=+1, surface=surfaces['BP Radius-3'])
    pincells[group][name]['bp']['bg'].addSurface(halfspace=-1, surface=surfaces['BP Radius-4'])
    
    # AIR2
    pincells[group][name]['bp']['helium2'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['helium'].getId(), sectors=8)
    pincells[group][name]['bp']['helium2'].addSurface(halfspace=+1, surface=surfaces['BP Radius-4'])
    pincells[group][name]['bp']['helium2'].addSurface(halfspace=-1, surface=surfaces['BP Radius-5'])
    		
    # SS3041
    pincells[group][name]['bp']['ss1'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['ss304'].getId(), sectors=8)
    pincells[group][name]['bp']['ss1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-5'])
    pincells[group][name]['bp']['ss1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-6'])
    
    # WATER
    pincells[group][name]['bp']['water'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['water'].getId(), sectors=8)
    pincells[group][name]['bp']['water'].addSurface(halfspace=+1, surface=surfaces['BP Radius-6'])
    pincells[group][name]['bp']['water'].addSurface(halfspace=-1, surface=surfaces['BP Radius-7'])
    
    # CLAD
    pincells[group][name]['bp']['cladding'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['cladding'].getId(), sectors=8)
    pincells[group][name]['bp']['cladding'].addSurface(halfspace=+1, surface=surfaces['BP Radius-7'])
    pincells[group][name]['bp']['cladding'].addSurface(halfspace=-1, surface=surfaces['BP Radius-8'])
    
    # WATER
    pincells[group][name]['bp']['water1'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material= materials[group][name]['water'].getId(), sectors=8)
    pincells[group][name]['bp']['water1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-8'])
    
		

