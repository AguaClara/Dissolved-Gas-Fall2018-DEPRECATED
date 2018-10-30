# Python code for the minimum fluidization flow rate of the prototype fluidized bed reactor. In the future, adjustments will be made to the code to indicate the RPM setting for the peristaltic pump that the subteam will use to pump water into the system.

# In this file, the code requests porosity as an input, rather than the mass of sand, height of the bed, and the mass of the sand in the bed.

# This code makes use of aide_design, a package provided by AguaClara Cornell.

# Assumptions: All input values are real numbers.

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design import*

# The following code, determining the bed's minimum flow for fluidization, adheres to the equation in Source 4 in the Fluidization page of the Literature folder (i.e. Fluidization Source 4). The code requests the reactor's cross sectional area in order to calculate the fluidization flow rate at the end of the script.

area_reactor = float(input("What is the cross sectional area of the fluidized bed reactor, in units of millimeters squared?"))
porosity = float(input("What is the porosity of the sand bed?"))

density_sand = float(input("What is the density of the sand, in units of kilograms per cubic meter?"))
diameter = float(input("What is the average diameter of the sand grains, in units of millimeters?"))
density_water = 997 #Implicit units are kilograms per cubic meter

kozeny = 5 #This is an approximate value, suggested by Fluidization Source 4
viscosity = float(input("What is the kinematic viscosity of water, in units of millimeters squared per second?"))

# The following variable definitions are based off those in the squation in Fluidization Source 4.
# Integers such as 1000 serve as implicit conversion factors between units.

fluidization_velocity_FirstTerm = (porosity**3 * 9.8 * (diameter/1000)**2)/(36*kozeny*(viscosity/1000**2)*(1-porosity))

fluidization_velocity_SecondTerm = (density_sand/density_water - 1)

fluidization_velocity = fluidization_velocity_FirstTerm * fluidization_velocity_SecondTerm

fluidization_flow = fluidization_velocity * area_reactor

#The following line of code truncates the flow rate to three significant figures.
edited_result = ut.sig(fluidization_flow,3)

print("The minimum flow required for fluidization is "+ str(edited_result) +" mL/s.")
