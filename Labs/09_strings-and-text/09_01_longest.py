# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

print(len(longest_german_word),"longest german")
print("\n")
print(len(longest_hungarian_word),"longest hungarian")
print("\n")
print(len(longest_finnish_word),"longest finish")
print("\n")
print(len(strong_password),"password")
print("\n")

"""lista=[longest_german_word,longest_hungarian_word,longest_finnish_word,strong_password]

def get_max_length(lst):
    return len(max(lst, key=len))

long_max=get_max_length(lista)

print("la mas larga es: ",long_max)"""
