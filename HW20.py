#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW20


#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    y = int(input("Please select a number that will divide into 100"))
    x = 100/y
except:
    print("cannot divide by 0")


#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    numberinput = int(input("Enter any number"))
except ValueError:
    print("error given answer is not an integer")



#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
c = 5
while c <= 5:
    print(c)
    c -= 1
    if c <0:
        raise Exception("Number is below zero")


