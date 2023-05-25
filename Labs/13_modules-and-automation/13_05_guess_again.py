# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num=random.randint(1,10)
count=5

guess=int(input("Please enter a number: "))

while count!=0:
    count-=1
    
    if guess==num:
        print("Congratulations you guessed the number")
        break

    elif count==0:
        print("sorry but you don`t have more attempts, game over")
        break
    
    else:
        print("Sorry that`s not the number, try again")
        print("You still have",count,"attempts to guess it")

    guess=int(input("Please enter a number: "))

