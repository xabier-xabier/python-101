# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

for i in range(1,1001,1):
    if i%1==0 and i%5==0:
        print(i)

