# Print out every prime number between 1 and 1000.

for i in range(1,1001,1):
    if i==1:
        i+=1
    elif i==2:
        print(i)
    elif i==3:
        print(i)
    elif i%1==0 and i%i==0 and i%2!=0 and i%3!=0:
        print(i)

