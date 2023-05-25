# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

a=20
a=float(a)
#print(type(a))
#print(a)

a=int(a)
#print(type(a))
#print(a)

b=20.0
c=a/b

print(type(c))
print(c)     #int information is lost in any interaction with floats

mult=c*a

print(type(mult))

