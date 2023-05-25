# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

from pathlib import Path

#locate in the desktop the path
desktop = Path().home().joinpath("Desktop\coding nomads").joinpath("tasks")

#for loop to find and print 

for char in desktop.iterdir():
    if char.suffix==".py":
        print(f"{char.name:>15}")


