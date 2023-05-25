# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

text=input("Please write a sentence: ")

count_a=0
count_e=0
count_i=0
count_o=0
count_u=0

for i in text:
    if i=="a" or i=="A":
        count_a +=1
    elif i=="e" or i=="E":
        count_e +=1
    elif i=="i" or i=="I":
        count_i +=1
    elif i=="o" or i=="O":
        count_o +=1
    elif i=="u" or i=="U":
        count_u +=1

print("number of 'a' : ",count_a)
print("\n")
print("number of 'e' : ",count_e)
print("\n")
print("number of 'i' : ",count_i)
print("\n")
print("number of 'o' : ",count_o)
print("\n")
print("number of 'u' : ",count_u)
print("\n")