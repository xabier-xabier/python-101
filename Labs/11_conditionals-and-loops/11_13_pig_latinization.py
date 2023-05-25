# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

poem_="""You would never guess what can happen when you jump into a seemingly shallow puddle at night time!
It turns out that it is not a puddle rather than a giant hole which brings you to a new world on the other side of the light water. Now you are left stunning and don't know what to do.
So you decide to call Whoolio who lives in Never Never land.
 """
poem="You would never guess what can happen"

#words=poem.split()
length=len(poem)
blank=[0,]
j=0

for i in poem:                  #Find blank spaces
    if i==" ":
        blank.append(j)

    j=j+1

z=1
leng_blank=len(blank)
y=0
list=[]

for i in range(0,leng_blank,1):
    if z<leng_blank and y!=0:
        num=blank[z]
        num1=blank[y]+1
        num2=num1+1
        list.append(poem[num2:num]+poem[num1]+"ay")

    elif z<leng_blank and y==0:
        num=blank[z]
        num1=blank[y]
        num2=num1+1
        list.append(poem[num2:num]+poem[num1]+"ay")

    elif z==leng_blank:
        num=length
        num1=blank[y]+1
        num2=num1+1
        list.append(poem[num2:num]+poem[num1]+"ay")

    y+=1
    z+=1

print(blank)
print(list)




