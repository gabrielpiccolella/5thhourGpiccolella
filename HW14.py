#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW14


#1. Create a variable that asks the user for an integer and an empty integer variable.

userinput = int(input("Select a number between one and ten"))

numb = 0




#2. Create a loop with a range from 1 to the number the user input.
for k in range(1, userinput + 1,):
    print(k)
    continue
#3. Use the loop to find the factorial of that number. A factorial of a number is that number multiplied
#by every number before it until you reach 1.
#For example: 5! is 5 x 4 x 3 x 2 x 1 = 120
def factorial(userinput):
    if userinput < 0:
        print("Not defined for negative numbers.")
        return
    elif userinput == 0:
        return 1
    else:
        result = 1
        for i in range(1, userinput + 1):
            result *= i
        return result
#4. Print the factorial.
print(factorial(userinput))