# Python code for standard deviation of a list of length 100 or less
# Assumption: All entries are real numbers

import math

values = []
item = "blank"
for n in range(100):
    item = input("What item would you like to add to the list? If the list is complete, type 'quit' ")
    if item == "quit":
        break
    else:
        values.append(float(item))

total=0
for n in range(len(values)):
    total += values[n]

average= total / len(values)

numerator = 0
for n in range(len(values)):
    numerator += (values[n]-average)**2

standard_deviation = math.sqrt(numerator / (len(values)-1))
print("The standard deviation in the given list is " + str(standard_deviation))
