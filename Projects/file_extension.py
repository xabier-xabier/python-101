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

lista=[file_1.endswith("pdf"),file_2.endswith("pdf"),file_3.endswith("pdf"),file_4.endswith("pdf")]
file_list=["file_1","file_2","file_3","file_4"]

j=0

for i in lista:
    if i==True:
        print(file_list[j],"is a pdf")
        j=j+1
        
    else:
        print(file_list[j],"is not a pdf")
        j=j+1
        

print("\n")
print("File_1 = ",text1)
print("File_2 = ",text2)
print("File_3 = ",text3)
print("File_4 = ",text4)

