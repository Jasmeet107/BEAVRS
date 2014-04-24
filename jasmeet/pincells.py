from openmoc import CellBasic, universe_id
from surfaces import surfaces
#import materials

pincells = dict() #dictionary of pin cells


################################################################################
#############################  1.6% Enriched Fuel Pins #########################
################################################################################

pincells['16fuel'] = {} #dictionary of cells within this particular pin cell
pincells['16fuel']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['16fuel']['fuel'] = CellBasic(universe=pincells['16fuel']['uid'], material=0) #dummy material #initializes fuel cell
pincells['16fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

#CLADDING
pincells['16fuel']['clad'] = CellBasic(universe=pincells['16fuel']['uid'], material=1) #initializes cladding cell
pincells['16fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
pincells['16fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

#WATER
pincells['16fuel']['water'] = CellBasic(universe=pincells['16fuel']['uid'], material=2)  
pincells['16fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
pincells['16fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of 3rd circle 

################################################################################
#############################  2.4% Enriched Fuel Pins #########################
################################################################################

pincells['24fuel'] = {} #dictionary of cells within this particular pin cell
pincells['24fuel']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['24fuel']['fuel'] = CellBasic(universe=pincells['24fuel']['uid'], material=3) 
pincells['24fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

#CLADDING
pincells['24fuel']['clad'] = CellBasic(universe=pincells['24fuel']['uid'], material=4) 
pincells['24fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
pincells['24fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

#WATER
pincells['24fuel']['water'] = CellBasic(universe=pincells['24fuel']['uid'], material=5) 
pincells['24fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
pincells['24fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of 3rd circle

################################################################################
#############################  3.1% Enriched Fuel Pins #########################
################################################################################

pincells['31fuel'] = {} #dictionary of cells within this particular pin cell
pincells['31fuel']['uid'] = universe_id() #sets universe ID for pin cell

#FUEL
pincells['31fuel']['fuel'] = CellBasic(universe=pincells['31fuel']['uid'], material=6) 
pincells['31fuel']['fuel'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-1']) #inside of innermost circle

#CLADDING
pincells['31fuel']['clad'] = CellBasic(universe=pincells['31fuel']['uid'], material=7) 
pincells['31fuel']['clad'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-1']) #outside of innermost (1st) circle
pincells['31fuel']['clad'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-2']) #inside of 2nd circle

#WATER
pincells['31fuel']['water'] = CellBasic(universe=pincells['31fuel']['uid'], material=8) 
pincells['31fuel']['water'].addSurface(halfspace=+1, surface=surfaces['Fuel Radius-2']) #outside of 2nd circle
pincells['31fuel']['water'].addSurface(halfspace=-1, surface=surfaces['Fuel Radius-3']) #inside of 3rd circle


################################################################################
##########################  Guide Tube Pin Cells ###############################
################################################################################

pincells['guidetube'] = {} #dictionary of cells within this guide tube
pincells['guidetube']['uid'] = universe_id() #sets universe ID for pin cell

#WATER
pincells['guidetube']['water'] = CellBasic(universe=pincells['guidetube']['uid'], material=9) 
pincells['guidetube']['water'].addSurface(halfspace=-1, surface=surfaces['GT Radius-1']) #inside of innermost circle

#CLADDING
pincells['guidetube']['clad'] = CellBasic(universe=pincells['guidetube']['uid'], material=10) 
pincells['guidetube']['clad'].addSurface(halfspace=+1, surface=surfaces['GT Radius-1']) #outside of innermost circle
pincells['guidetube']['clad'].addSurface(halfspace=-1, surface=surfaces['GT Radius-2']) #inside of 2nd circle


################################################################################
#######################  Instrument Tube Pin Cells  ############################
################################################################################
pincells['instube'] = {} #dictionary of cells within this guide tube
pincells['instube']['uid'] = universe_id() #sets universe ID for pin cell

#AIR
pincells['instube']['air'] = CellBasic(universe=pincells['instube']['uid'], material=11) 
pincells['instube']['air'].addSurface(halfspace=-1, surface=surfaces['IT Radius-1']) #inside of innermost circle

#CLADDING
pincells['instube']['clad'] = CellBasic(universe=pincells['instube']['uid'], material=12) 
pincells['instube']['clad'].addSurface(halfspace=+1, surface=surfaces['IT Radius-1']) #outside of innermost circle
pincells['instube']['clad'].addSurface(halfspace=-1, surface=surfaces['IT Radius-2']) #inside of 2nd circle


################################################################################
#######################  Burnable Absorber Pin Cell  ###########################
################################################################################
pincells['bp'] = {} #dictionary of cells within this guide tube
pincells['bp']['uid'] = universe_id() #sets universe ID for pin cell


#AIR
pincells['bp']['air'] = CellBasic(universe=pincells['bp']['uid'], material=13) 
pincells['bp']['air'].addSurface(halfspace=-1, surface=surfaces['BP Radius-1']) #inside of innermost circle

#SS304
pincells['bp']['ss'] = CellBasic(universe=pincells['bp']['uid'], material=14) 
pincells['bp']['ss'].addSurface(halfspace=+1, surface=surfaces['BP Radius-1']) #outside of innermost circle
pincells['bp']['ss'].addSurface(halfspace=-1, surface=surfaces['BP Radius-2']) #inside of 2nd circle

#AIR1
pincells['bp']['air1'] = CellBasic(universe=pincells['bp']['uid'], material=15)  
pincells['bp']['air1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-2']) #outside of 2nd circle
pincells['bp']['air1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-3']) #inside of 3rd circle

#BOROSILICATE GLASS
pincells['bp']['bg'] = CellBasic(universe=pincells['bp']['uid'], material=16)  
pincells['bp']['bg'].addSurface(halfspace=+1, surface=surfaces['BP Radius-3']) #outside of 3rd circle
pincells['bp']['bg'].addSurface(halfspace=-1, surface=surfaces['BP Radius-4']) #inside of 4th circle

#AIR2
pincells['bp']['air2'] = CellBasic(universe=pincells['bp']['uid'], material=17)  
pincells['bp']['air2'].addSurface(halfspace=+1, surface=surfaces['BP Radius-4']) #outside of 4th circle
pincells['bp']['air2'].addSurface(halfspace=-1, surface=surfaces['BP Radius-5']) #inside of 5th circle

#SS3041
pincells['bp']['ss1'] = CellBasic(universe=pincells['bp']['uid'], material=18)  
pincells['bp']['ss1'].addSurface(halfspace=+1, surface=surfaces['BP Radius-5']) #outside of 5th circle
pincells['bp']['ss1'].addSurface(halfspace=-1, surface=surfaces['BP Radius-6']) #inside of 6th circle

#WATER
pincells['bp']['water'] = CellBasic(universe=pincells['bp']['uid'], material=19)  
pincells['bp']['water'].addSurface(halfspace=+1, surface=surfaces['BP Radius-6']) #outside of 6th circle
pincells['bp']['water'].addSurface(halfspace=-1, surface=surfaces['BP Radius-7']) #inside of 7th circle

#CLAD
pincells['bp']['clad'] = CellBasic(universe=pincells['bp']['uid'], material=20)  
pincells['bp']['clad'].addSurface(halfspace=+1, surface=surfaces['BP Radius-7']) #outside of 7th circle
pincells['bp']['clad'].addSurface(halfspace=-1, surface=surfaces['BP Radius-8']) #inside of 8th circle





