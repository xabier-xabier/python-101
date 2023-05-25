# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

num=int(input("Please choose a number between 1 and 1,000,000,000: "))

j=0

while j!=num:
    j+=1
    if j==num:
        print("The number chosen is: ",j)
        break


