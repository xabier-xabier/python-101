#Receive the following arguments from the user:
# -Kilometers to drive
# -Liters-per-kilometer usage of the car
# -Price per liter of fuel
#Calculate the cost of the trip and display it to the user in the console. 
#Apply some of the string formatting tricks that you learned about in this course section.

kilometers=float(input("Please enter the kilometers to drive: "))
liters=float(input("Please enter the liters per kilometer usage of the car: "))
price=float(input("Please enter the price per liter of fuel: "))

def calculation(km,lit,price):
    sum=km*lit*price
    return sum

final=calculation(kilometers,liters,price)

print("\n")

print(f"""If you want to drive for {kilometers} km, with {liters} l/km of usage of the car
and {price} $/l of price of the fuel, the cost of the trip is going to be = {final:.2f} $""")

