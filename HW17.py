#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random

def hello_world():
    print("Hello World!")

#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads
    global tails
    for i in range (1,101):
        flip = random.randint(1,2)
        if flip == 1:
            heads += 1
        elif flip == 2:
            tails+= 1




#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
coin_flip()


#5. Print the final result of heads and tails here
print("Amount of heads", heads)
print("Amount of tails", tails)

