# Write a function that computes the volume of a sphere given its radius.

import math

def sphere_vol(rad):
    volume = 4/3 * math.pi * rad**3
    # Or return it and print in function call
    print(round(volume, 1))

sphere_vol(5)