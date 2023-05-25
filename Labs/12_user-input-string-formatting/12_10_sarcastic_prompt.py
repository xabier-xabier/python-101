# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

text=input("Please tell me your honest opinion about global warming: ")

last=""

j=0
for i in text:

    if j==0:
        last+=i.upper()
        j+=1

    elif j%2==0:
        last+=i.upper()
        j+=1
        
    else:
        last+=i
        j+=1

print(last)



