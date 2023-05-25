# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime

t_now= datetime.now()

text=t_now.strftime("%B %d, %Y")
text1=t_now.strftime("%H:%M:%S")
print("date: ",text)
print("Time: ",text1)

# Textual month, day and year	
#date = today_d.strftime("%B %d, %Y")
#print("date =", date)

