#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -=1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
i = 0
while i % 2 == 0:
    print(i)
    i += 2
    if i >= 31:
        break


#3. Create a while loop that repeats until the user
#inputs the number 0.
n = int(input("enter a number"))

while n != 0:
    print(n)
    n = int(input("enter a new number"))


