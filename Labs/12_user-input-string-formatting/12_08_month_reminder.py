# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

intro=int(input("please write a number from 1-12: "))

month=["January","February","March","April","May",
       "June","July","August","September","October","November","December"]

if intro>12 or intro<0:
    intro=int(input("Error. Please choose a month between 1 to 12"))

else:
    print(month[intro-1])

