# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

intro=input("Please write a sentence: ")
symbol=input("please write one symbol: ")

sol=intro.replace(intro[0],symbol)

print(sol)
