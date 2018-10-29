# Python code for the minimum fluidization velocity of the prototype fluidized bed reactor
# In this alternative file, the code requests porosity for an input, rather than the mass of sand, height of the bed, and the mass of the sand in the bed.
# Assumptions: All input values are real numbers.

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut

area_reactor = float(input("What is the cross sectional area of the fluidized bed reactor, in units of millimeters squared?"))
density_sand = float(input("What is the density of the sand, in units of kilograms per cubic meter?"))
porosity = float(input("What is the porosity of the sand bed?"))

# The following code, determining the bed's minimum flow for fluidization, adheres to the equation in Source 4 in the Fluidization page of the Literature folder.
diameter = float(input("What is the average diameter of the sand grains, in millimeters?"))
kozeny = 5 #This is an approximate value, suggested by Fluidization Source 4
density_water = 997 #Implicit units are kilograms per cubic meter
viscosity = float(input("What is the kinematic viscosity of water, in units of millimeters squared per second?"))

fluidization_velocity_FirstTerm = (porosity**3 * 9.8 * (diameter/1000)**2)/(36*kozeny*(viscosity/1000**2)*(1-porosity))

fluidization_velocity_SecondTerm = (density_sand/density_water - 1)

fluidization_velocity = fluidization_velocity_FirstTerm * fluidization_velocity_SecondTerm

fluidization_flow = fluidization_velocity * area_reactor

edited_result = ut.sig(fluidization_flow,3)

print("The minimum flow required for fluidization is "+ str(edited_result) +", in units of milliliters per second")
