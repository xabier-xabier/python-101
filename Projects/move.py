#clean the desktop
# get my tools
from pathlib import Path

#locate the desktop
desktop = Path().home().joinpath("OneDrive\Escritorio")
print(desktop)

#create folder
desktop.joinpath("screenshots").mkdir(exist_ok=True)

#identify screenshots
for f in desktop.iterdir():
    if f.suffix==".png":
        #move the files
        f.replace(desktop.joinpath("screenshots").joinpath(f.name))




