# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

#sys.exit()
import sys

x=True

while x==True:
    text=int(input("Please enter a number: "))

    if text<10:
        sys.exit("The number is under 10, goodbye")
    else:
        print("The number is not less than 10")

