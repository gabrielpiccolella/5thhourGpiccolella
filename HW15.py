#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a def function that calculates the average of three numbers.
numbers = [1,2,3,4,5]

def average(numbers):
    print(sum(numbers) / len(numbers))

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animales(*animals):
    print("The third animals name is " + animals[2])

#4. Create a def function that loops from 1 to the number put in the argument.
def count(userinput):
    for k in range(1, userinput + 1, ):
        print(k)
        continue

#5. Call all of the functions created in 1 - 4 with relevant arguments.
hello_world()
average(numbers)
animales("Monkey", "Spider", "Bird", "Biggest Bird", "Octopus")
count(int(input("Enter a number")))