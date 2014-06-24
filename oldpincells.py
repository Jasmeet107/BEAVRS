from openmoc import CellBasic, universe_id
from surfaces import surfaces
from materials import materials

pincells = {} #dictionary of pin cells
groups = ['2', '8']
for group in groups:
  pincells[group] = {}

  pincells[group]['water'] = {}
  pincells[group]['water']['uid'] = universe_id() #sets universe ID for pin cell
  pincells[group]['water'] = CellBasic(universe=pincells[group]['water']['uid'], material= materials[group]['pwru160c00']['water'].getId())

	################################################################################
	#############################  1.6% Enriched Fuel Pins #########################
	################################################################################

  pincells[group]['pwru160c00'] = {}  #dictionary of cells within this particular pin cell
  pincells[group]['pwru160c00']['uid'] = universe_id() #sets universe ID for pin cell

  #FUEL
  pincells[group]['pwru160c00']['fuel'] = CellBasic(universe=pincells[group]['pwru160c00']['uid'], material= materials[group]['pwru160c00']['fuel'].getId() #initializes fuel cell
  pincells[group]['pwru160c00']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

  #HELIUM
  pincells[group]['pwru160c00']['helium'] = CellBasic(universe=pincells[group]['pwru160c00']['uid'], material= materials[group]['pwru160c00']['helium'].getId()) #initializes helium cell
  pincells[group]['pwru160c00']['helium'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
  pincells[group]['pwru160c00']['helium'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

  #CLADDING
  pincells[group]['pwru160c00']['cladding'] = CellBasic(universe=pincells[group]['pwru160c00']['uid'], material= materials[group]['pwru160c00']['cladding'].getId()) #initializes cladding cell
  pincells[group]['pwru160c00']['cladding'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
  pincells[group]['pwru160c00']['cladding'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of outermost circle
  
  #WATER
  pincells[group]['pwru160c00']['water'] = CellBasic(universe=pincells[group]['pwru160c00']['uid'], material= materials[group]['pwru160c00']['water'].getId() #initializes water cell
  pincells[group]['pwru160c00']['fuel'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-3']) #outside of outermost circle

	################################################################################
	#############################  2.4% Enriched Fuel Pins #########################
	################################################################################

	names = ['pwru240c00', 'pwru240w12', 'pwru240w16']

  for name in names:
    pincells[group][name] = {} #dictionary of cells within this particular pin cell
    pincells[group][name]['uid'] = universe_id() #sets universe ID for pin cell

   #FUEL
  pincells[group][name]['fuel'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['fuel'].getId() #initializes fuel cell
  pincells[group][name]['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

  #HELIUM
  pincells[group][name]['helium'] = CellBasic(universe=pincells[group]['helium']['uid'], material= materials[group][name]['helium'].getId()) #initializes helium cell
  pincells[group][name]['helium'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
  pincells[group][name]['helium'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

  #CLADDING
  pincells[group][name]['cladding'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['cladding'].getId()) #initializes cladding cell
  pincells[group][name]['cladding'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
  pincells[group][name]['cladding'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of outermost circle
  
  #WATER
  pincells[group][name]['water'] = CellBasic(universe=pincells[group][name]['uid'], material= materials[group][name]['water'].getId() #initializes water cell
  pincells[group][name]['fuel'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-3']) #outside of outermost circle

	################################################################################
	#############################  3.1% Enriched Fuel Pins #########################
	################################################################################

	names = ['pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']
	
  for name in names:
    pincells[group][name] = {} #dictionary of cells within this particular pin cell
    pincells[group][name]['uid'] = universe_id() #sets universe ID for pin cell

    #FUEL
    pincells[group][name]['fuel'] = CellBasic(universe=pincells[group][name]['uid'], material=materials[group][name]['fuel'].getId())
    pincells[group][name]['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

    #CLADDING
    pincells[group][name]['cladding'] = CellBasic(universe=pincells[group][name]['uid'], material=materials[group][name]['cladding'].getId())
    pincells[group][name]['cladding'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
    pincells[group][name]['cladding'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

    #WATER
    pincells[group][name]['water'] = CellBasic(universe=pincells[group][name]['uid'], material=materials[group][name]['water'].getId()) 
    pincells[group][name]['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
    pincells[group][name]['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of 3rd circle


	################################################################################
	##########################  Guide Tube Pin Cells ###############################
	################################################################################

	names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

  for name in names:
    pincells[group][name]['guidetube'] = {} #dictionary of cells within this guide tube
    pincells[group][name]['guidetube']['uid'] = universe_id() #sets universe ID for pin cell

    #WATER
    pincells[group][name]['guidetube']['water'] = CellBasic(universe=pincells[group][name]['guidetube']['uid'], material=materials[group][name]['water'].getId())
    pincells[group][name]['guidetube']['water'].addSurface(halfspace=-1, surface=surfaces['GT Radius-1']) #inside of innermost circle

    #CLADDING
    pincells[group][name]['guidetube']['cladding'] = CellBasic(universe=pincells[group][name]['guidetube']['uid'], material=materials[group][name]['cladding'].getId())
    pincells[group][name]['guidetube']['cladding'].addSurface(halfspace=+1, surface=surfaces['GT Radius-1']) #outside of innermost circle
    pincells[group][name]['guidetube']['cladding'].addSurface(halfspace=-1, surface=surfaces['GT Radius-2']) #inside of 2nd circle


	################################################################################
	#######################  Instrument Tube Pin Cells  ############################
	################################################################################

	names = ['pwru160c00','pwru240c00','pwru240w12', 'pwru240w16', 'pwru310c00', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

  for name in names:
    pincells[group][name]['instube'] = {} #dictionary of cells within this guide tube
    pincells[group][name]['instube']['uid'] = universe_id() #sets universe ID for pin cell

    #AIR
    pincells[group][name]['instube']['helium'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material=materials[group][name]['helium'].getId())
    pincells[group][name]['instube']['helium'].addSurface(halfspace=-1, surface=surfaces['IT Radius-1']) #inside of innermost circle

    #CLADDING
    pincells[group][name]['instube']['cladding'] = CellBasic(universe=pincells[group][name]['instube']['uid'], material=materials[group][name]['cladding'].getId())
    pincells[group][name]['instube']['cladding'].addSurface(halfspace=+1, surface=surfaces['IT Radius-1']) #outside of innermost circle
    pincells[group][name]['instube']['cladding'].addSurface(halfspace=-1, surface=surfaces['IT Radius-2']) #inside of 2nd circle


	################################################################################
	#######################  Burnable Absorber Pin Cell  ###########################
	################################################################################

	names = ['pwru240w12', 'pwru240w16', 'pwru310w06', 'pwru310w12', 'pwru310w15', 'pwru310w16', 'pwru310w20']

  for name in names:
    pincells[group][name]['bp'] = {} #dictionary of cells within this guide tube
    pincells[group][name]['bp']['uid'] = universe_id() #sets universe ID for pin cell

    #AIR
    pincells[group][name]['bp']['helium'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['helium'].getId())
    pincells[group][name]['bp']['helium'].addSurface(halfspace=-1, surface=surfaces['BP Radius-1']) #inside of innermost circle

    #SS304
    pincells[group][name]['bp']['ss'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['ss304'].getId())
    pincells[group][name]['bp']['ss'].addSurface(halfspace=+1, surface=surfaces['BP Radius-1']) #outside of innermost circle
    pincells[group][name]['bp']['ss'].addSurface(halfspace=-1, surface=surfaces['BP Radius-2']) #inside of 2nd circle

    #AIR1
    pincells[group][name]['bp']['helium1'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['helium'].getId())
    pincells[group][name]['bp']['helium1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-2']) #outside of 2nd circle
    pincells[group][name]['bp']['helium1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-3']) #inside of 3rd circle

    #BOROSILICATE GLASS
    pincells[group][name]['bp']['bg'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['bp'].getId())
    pincells[group][name]['bp']['bg'].addSurface(halfspace=+1, surface=surfaces['BP Radius-3']) #outside of 3rd circle
    pincells[group][name]['bp']['bg'].addSurface(halfspace=-1, surface=surfaces['BP Radius-4']) #inside of 4th circle

    #AIR2
    pincells[group][name]['bp']['helium2'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['helium'].getId())
    pincells[group][name]['bp']['helium2'].addSurface(halfspace=+1, surface=surfaces['BP Radius-4']) #outside of 4th circle
    pincells[group][name]['bp']['helium2'].addSurface(halfspace=-1, surface=surfaces['BP Radius-5']) #inside of 5th circle

    #SS3041
    pincells[group][name]['bp']['ss1'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['ss304'].getId())
    pincells[group][name]['bp']['ss1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-5']) #outside of 5th circle
    pincells[group][name]['bp']['ss1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-6']) #inside of 6th circle

    #WATER
    pincells[group][name]['bp']['water'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['water'].getId())
    pincells[group][name]['bp']['water'].addSurface(halfspace=+1, surface=surfaces['BP Radius-6']) #outside of 6th circle
    pincells[group][name]['bp']['water'].addSurface(halfspace=-1, surface=surfaces['BP Radius-7']) #inside of 7th circle

    #CLAD
    pincells[group][name]['bp']['cladding'] = CellBasic(universe=pincells[group][name]['bp']['uid'], material=materials[group][name]['cladding'].getId())
    pincells[group][name]['bp']['cladding'].addSurface(halfspace=+1, surface=surfaces['BP Radius-7']) #outside of 7th circle
    pincells[group][name]['bp']['cladding'].addSurface(halfspace=-1, surface=surfaces['BP Radius-8']) #inside of 8th circle
