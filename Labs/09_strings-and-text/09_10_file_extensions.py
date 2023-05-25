# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

text1=file_1[-3:]
text2=file_2[-3:]
text3=file_3[-3:]
text4=file_4[-3:]

lista=[text1,text2,text3,text4]
file_list=["file_1","file_2","file_3","file_4"]

j=0

for i in lista:
    if i=="pdf":
        print(file_list[j],"is a pdf")
        j=j+1
        
    else:
        print(file_list[j],"is not a pdf")
        j=j+1
        

print("File_1 = ",text1)
print("File_2 = ",text2)
print("File_3 = ",text3)
print("File_4 = ",text4)