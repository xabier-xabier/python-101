# Demonstrate the use of all logical operators (and, or, not) below.
# Create variables that hold boolean values, then combine them
# to express the following sentence:
#
#   do two wrongs make a right?
# 
# Note that the truth value of the statement doesn't matter,
# but try to use all three logical operators in one line of code
# to get another boolean value as your result :)

wrong = False
right = True

do=False
two=True

make=True
a=True

if do !=two and wrong==False:
    sentence1=" do two wrongs "

if make==a or a==right:
    sentence2= "make a right?"

sentence=sentence1+sentence2

print(sentence)

    

