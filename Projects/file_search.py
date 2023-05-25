#Write a script that searches a folder you specify (as well as its subfolders, up to two levels deep) 
#and compiles a list of all .jpg files contained in there. 
#The list should include the complete path of each .jpg file.

#Using for loops
#Using conditional statements
#Working with pathlib
#Thinking about nested loops

from pathlib import Path

text=input("Please enter the name of the folder you want to search: ")

desktop=Path().home().joinpath("Desktop")
loc=desktop.joinpath(text)
loc1=loc.joinpath("Prueba")


#For loop find and print of the specified folder

for char in loc.iterdir():
    if char.suffix==".jpg":
        name=char.name
        print(f"{name}------>{loc}")

#For loop in subfolder    
for char in loc.iterdir():
    x=str(char)
    if x.find(".")==-1:
        loc1=loc.joinpath(char)
        for char1 in loc1.iterdir():
            if char1.suffix==".jpg":
                name1=char1.name
                print(f"{name1}------>{loc1}")
    
    elif x.find(".")!=-1:
        pass









