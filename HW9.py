#Name:
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!

#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#Calculate Temperature
#Make nested if statements in regards to the temperature
#Close all if statements with "Thank you"

import random

temp = random.randint(1,35)

print("It is", temp, "celcius outside right now")

if temp > 20:
    print("Its hot!")
elif temp >= 10 :
    print("Its mild")
else:
    print("Its cold!")
print("Thank you!")
