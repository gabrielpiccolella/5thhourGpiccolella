#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW6

#1. Print Hello World!
print("Hello World!")

#2. Create a variable named num and assign it a variable.
import random

num = random.randint(1,100)
print(num)
#3. Create a nested if statement follows this structure:

if num % 2 == 0:
   if  num % 3 == 0:
      print (num//2)
      print(num//3)
   elif num % 2 == 0:
       print ("that it is not divisible by 3")
       print(num//2)
else:
   if num % 3 == 0:
       print("num is not divisible by 2")
       print(num//3)
   else:
       print("num is not divisible by 2 or 3")
