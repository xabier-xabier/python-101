# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

intro=input("Please enter your name: ")

result=intro.split()

print("Hello", result[0], " nice to interact with you")