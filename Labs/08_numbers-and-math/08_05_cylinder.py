# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
from numpy import pi

r=3.14
h=5

def surf_area(r,h):
    cal=2*pi*r*h
    return cal

def vol(r,h):
    cal=pi*h*r**2
    return cal

area=surf_area(r,h)
volume=vol(r,h)

print("The surface area value is:",area)
print("\n")
print("The volume values is:",volume)





