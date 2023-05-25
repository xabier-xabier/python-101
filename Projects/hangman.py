# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

hard_code="Satanas"

print("Is a powerful person and is always angry")
print("""You have 6 chances to guess the name. 
        Just type 1 letter each time""")
print("\n")
print("sequence of blanks of the name: _ _ _ _ _ _ _")
print("\n")
trial=input("Please enter a letter: ")

count=6

guess=False
guess_a=False
guess_s=False
guess_t=False
guess_n=False

show="_ _ _ _ _ _ _"

show_=list(show)

while count!=0 and guess==False:

    if len(trial)!=1:
        print("Error, only one letter can be chosen each time")
    
    else:
        if trial=="a":
            show_[2]="a"
            show_[6]="a"
            show_[10]="a"
            guess_a=True
            show=''.join(show_)
            print(show)
            count-=1
            #trial=input("Please enter a letter: ")

        elif trial=="s":
            show_[0]="S"
            show_[12]="s"
            guess_s=True
            show=''.join(show_)
            print(show)
            count-=1
            #trial=input("Please enter a letter: ")

        elif trial=="t":
            show_[4]="t"
            guess_t=True
            show=''.join(show_)
            print(show)
            count-=1

        elif trial=="n":
            show_[8]="n"
            guess_n=True
            show=''.join(show_)
            print(show)
            count-=1

        else:
            print("That letter is not in the the name to guess")
            print(show)
            count-=1

    if guess_a==True and guess_n==True and guess_s==True and guess_t==True and count!=0:
        guess==True
        print("congratulations you guessed the word")
        break

    elif count==0:
        print("Sorry there aren`t more chances to guess the word")
        break       
    
    print("You still have",count," chances to guess the word")
    trial=input("Please enter a letter: ")    

    





