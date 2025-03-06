#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class storestuff:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def double_price(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
redbull = storestuff(20,4, 2)
mango = storestuff(30, 1, 3)
chips = storestuff(16, 2, 1)

#3. Print the stock of all three objects and the cost of the second store item.
print("the stock of all items in the store is this many redbulls",  redbull.stock,  "This many mangos", mango.stock ,"& this many chips", chips.stock)
print("The cost of the mango is", mango.cost)

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.

mango.double_price()
print(f"new mango price {mango.cost}")

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
chips.stock = 4
print(f"New chip stock is {chips.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del redbull

try:
    print(redbull.weight)

except:
    print("RedBull out of stock Nick will be sad")

