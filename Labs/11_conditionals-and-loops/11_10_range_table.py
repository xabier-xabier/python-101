# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

list1=[]
list2=[]
list3=[]
list4=[]
list5=[]

for i in range(0,50,1):
    if i<10:
        list1.append(i)
    elif 9<i<20:
       list2.append(i)
    elif 19<i<30:
        list3.append(i)
    elif 29<i<40:
        list4.append(i)
    elif 39<i<50:
        list5.append(i)

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)



