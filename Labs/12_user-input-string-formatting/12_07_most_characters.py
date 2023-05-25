# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

# 3 scripts
text1=input("write the first sentence: ")
text2=input("Write the second sentence: ")
text3=input("Write the third sentence: ")

# Length of each sentence
leng1=len(text1)
leng2=len(text2)
leng3=len(text3)

# Comparison
if leng1>leng2 and leng1>leng3:
    print(leng1,"," ,text1)

elif leng2>leng1 and leng2>leng3:
        print(leng2,",", text2)
else:
      print(leng3,",",text3)


