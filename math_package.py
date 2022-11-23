# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*pow(r,2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
phi=12
dist=r*radians(phi)

# Print out dist
print(dist)