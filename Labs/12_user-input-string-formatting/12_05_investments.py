# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment=int(input("Please enter the investement amount: "))
rate=int(input("Please enterthe rate in percentage(%): "))
years=int(input("Please enter the number of years: "))

for i in range(1,years+1,1):
    profit=investment*(rate/100)
    investment+=profit

print(investment)
