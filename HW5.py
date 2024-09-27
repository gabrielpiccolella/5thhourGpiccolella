#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW5

#1. Print "Hello World!"
print("Hello World!")

#2. Create a list that contains 3 integers

import random

numList = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]

print("Here are your generated numbers", numList)
#3. Create an if statement that prints out whichever of the three numbers is the highest
if numList[0] > numList[1] and numList[0] > numList[2]:
    print("The first integer in the list is the highest number in the list.")
elif numList[1] > numList[0] and numList[1] > numList[2]:
    print("The second integer in the list is the highest number in the list.")
else:
    print("The third integer is the highest number in the list.")

