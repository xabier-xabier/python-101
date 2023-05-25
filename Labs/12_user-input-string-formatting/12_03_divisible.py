# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

intro=int(input("select a number betwen 1-1,000,000,000: "))

result=intro%3

if result==0:
    print(intro," is divisible by 3")

else:
    print(intro, " is not divisible by 3")