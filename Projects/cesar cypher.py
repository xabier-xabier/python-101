
text=str(input("Enter your text"))
print("\n")
cipher=int(input("Enter a displacement value"))

alphabet="abcdefghijklmnñopqrstuvwxyz"

length=len(alphabet)

sol=""


for a in text:
    loc=alphabet.find(a)

    if a==" ":
        sol+=" "

    else:

        if loc + cipher < length:
            sol+=alphabet[loc+cipher]
        else:
            sum = loc+cipher-length
            sol+=alphabet[sum]

print(sol)

