#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math


x = int(input("Input the radius of a sphere."))

y = (x**3)*(math.pi)*(4/3)


print(f'the volume of a sphere with a radius of {x} is equal to {y}')
