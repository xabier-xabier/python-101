# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

text=input("Write a text to be checked: ")
letter_input=input("write a letter please: ")

result=text.index(letter_input)

print(result)