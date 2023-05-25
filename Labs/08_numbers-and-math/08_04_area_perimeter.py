# Write code to display the area and perimeter
# of a rectangle that has a width of 2.4 and a height of 6.4.

width=2.4
height=6.4

def area(width,height):
    a=width*height
    return a

def perimeter(width,height):
    b=2*width+2*height
    return b

area_=area(width,height)
perimeter_=perimeter(width,height)

print("The area is:",area_)
print("\n")
print("The perimeter is:",perimeter_)

