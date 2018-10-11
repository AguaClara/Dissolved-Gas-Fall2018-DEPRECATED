# Python code for the minimum fluidization velocity of the prototype fluidized bed reactor

# Assumptions: All input values are real numbers.

import math

# The following code, determining the bed's porosity, adheres to the equation in Source 1 in the Fluidization page of the Literature folder
area = input("What is the cross sectional area of the reactor, in square centimeters?")
height = input("What is the height of the bed, in centimeters?")
density_sand = input("What is the density of the sand, in units of grams per cubic centimeter?")
mass = input("What is the total mass of sand in the reactor, in units of grams?")

porosity = 1 - (mass / (density_sand * area * height))
#The value of this may be 0.4, according to Source 4

# The following code, determining the bed's minimum flow for fluidization, adheres to the equation in Source 4 in the Fluidization page of the Literature folder.
diameter = input("What is the average diameter of the sand grains, in meters?")
kozeny = 5 #This is an approximate value, suggested by Source 4
density_water = 0.997 #Implicit units are grams per cubic centimeter
viscosity = input("What is the kinematic viscosity of ______?")

fluidization_velocity_FirstTerm = (porosity**3 * 9.8 * diameter**2)/(36*kozeny*viscosity*(1-porosity))

fluidization_velocity_SecondTerm = (density_sand/density_water - 1)

fluidization_velocity = fluidization_velocity_FirstTerm * fluidization_velocity_SecondTerm

fluidization_flow = fluidization_velocity * area * (100**2)

print("The minimum flow required for fluidization is "+ str(fluidization_flow) +", in units of milliliters per second")
