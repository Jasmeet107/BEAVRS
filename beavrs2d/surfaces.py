from openmoc import *


# Keys are Surface string names and values are OpenCSG Surfaces.
surfaces = {}


################################################################################
#############################  Fuel Pin Cell  ##################################
################################################################################

surfaces['Fuel Radius-1'] = Circle(x=0.0, y=0.0, radius=0.39218)
surfaces['Fuel Radius-2'] = Circle(x=0.0, y=0.0, radius=0.40005)
surfaces['Fuel Radius-3'] = Circle(x=0.0, y=0.0, radius=0.45720)


################################################################################
##########################  Guide Tube Pin Cell  ###############################
################################################################################

surfaces['GT Radius-1'] = Circle(x=0.0, y=0.0, radius=0.56134)
surfaces['GT Radius-2'] = Circle(x=0.0, y=0.0, radius=0.60198)


################################################################################
#######################  Instrument Tube Pin Cell  #############################
################################################################################

surfaces['IT Radius-1'] = Circle(x=0.0, y=0.0, radius=0.43688)
surfaces['IT Radius-2'] = Circle(x=0.0, y=0.0, radius=0.48387)
surfaces['IT Radius-3'] = Circle(x=0.0, y=0.0, radius=0.56134)
surfaces['IT Radius-4'] = Circle(x=0.0, y=0.0, radius=0.60198)



################################################################################
#######################  Burnable Absorber Pin Cell  ###########################
################################################################################

surfaces['BP Radius-1'] = Circle(x=0.0, y=0.0, radius=0.21400)
surfaces['BP Radius-2'] = Circle(x=0.0, y=0.0, radius=0.23051)
surfaces['BP Radius-3'] = Circle(x=0.0, y=0.0, radius=0.24130)
surfaces['BP Radius-4'] = Circle(x=0.0, y=0.0, radius=0.42672)
surfaces['BP Radius-5'] = Circle(x=0.0, y=0.0, radius=0.43688)
surfaces['BP Radius-6'] = Circle(x=0.0, y=0.0, radius=0.48387)
surfaces['BP Radius-7'] = Circle(x=0.0, y=0.0, radius=0.56134)
surfaces['BP Radius-8'] = Circle(x=0.0, y=0.0, radius=0.60198)


