#Ask the player for their name.
#Display a message that greets them and introduces them to the game world.
#Present them with a choice between two doors.
#If they choose the left door, they'll see an empty room.
#If they choose the right door, then they encounter a dragon.
#In both cases, they have the option to return to the previous room or interact further.
#When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
#When encountering the dragon, they have the choice to fight it.
#If they have the sword from the other room, then they will be able to defeat it and win the game.
#If they don't have the sword, then they will be eaten by the dragon and lose the game.


intro=input("Welcome to dragon fight game, enter a username please ")
print("Let`s have fun playing ",intro)

select=input("You have 2 doors in front of you, one in the right side another in left side, chosse 'right' or 'left '")

life=1
sword=False
leave=False
dragon=True

while life>0 and dragon==True:
    
    if select=="right" or select=="left":
        leave=False

        while leave==False:

            if select=="left" and leave==False and life!=0:
                print("This is an empty room")
                print("do you want to 'look' around or 'return' to previous room?")
                select=input("'look' or 'return'?")
                if select=="look" and leave==False:
                    print("you found a sword, good for beating dragons")
                    sword=True
                    print("you can have a look in the room or leave")
                    select=input("'look' or 'leave'")
                    while select=="look":
                        select=input("'look' or 'leave'")
                    if select=="leave":
                        leave=True
                
            elif select=="right" and leave==False and life!=0:
                print("There is a dragon in this room")
                print("do you want to 'fight' the dragon or 'leave' the room?")
                select=input("'fight' or 'leave'")
                if select=="fight" and sword==True:
                    print("Congratulations you beat the dragon")
                    dragon=False
                    break
                elif select=="fight" and sword==False:
                    print("Bad choice, you are not holding the sword....")
                    print("Game over")
                    life=0
                    break
                else: 
                    leave=True

    else:
        select=input("please choose 'right' or 'left'")



        

