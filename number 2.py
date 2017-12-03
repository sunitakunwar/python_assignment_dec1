'''Write a Python program which accepts the radius of a circle from the user and compute the area.'''

from math import pi

r = float(input ("enter a radius:"))

A = (pi*r*r)
print("The area is:%.3f" %A )
