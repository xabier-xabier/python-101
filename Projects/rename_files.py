# import library
from pathlib import Path

#desktop path
desktop=Path.home().joinpath("Desktop")

#Desired folder location
text=input(("Please enter the name of the folder you want to check: "))

loc=desktop.joinpath(text)
j=0

for char in loc.iterdir():
    if char.is_file():
        j+=1
        old_name = char.stem
        old_extension = char.suffix
        directory = loc
        new_name = "test" + str(j) + old_extension

        char.rename(Path(directory, new_name))
        print(char)


