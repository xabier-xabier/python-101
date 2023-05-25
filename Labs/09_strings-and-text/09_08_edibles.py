# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

"""print(s.find("butter"))  #pos 57
print(len("butter"))     # 6 length"""

word1 = s[57:57+6]

"""
print(s.find("leg"))        #pos 25
print(len("leg"))           # 3 length"""

word2=s[25:25+3]

"""
print(s.find("flour"))       #pos 68
print(len("flour"))            # 5lenght"""

word3=s[68:68+5]

sentence= word1+" "+word2+" "+word3
print(sentence)


