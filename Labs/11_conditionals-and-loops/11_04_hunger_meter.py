# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.


hunger = 2

if type(hunger) != str:
    print("declare your hunger levels with a string")

elif hunger == "small":
    print("Eat the apple")

else:
    print("Your hunger level is already defined by a string")

