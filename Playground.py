#Gabriel Piccolella
#5th Hour
#Playground HW

"""
#Defining the Name of the Adventurer
print("Hello Adventurer!")
print("My name is Merlin the Wise, tell me how shall i refer to thee?")
name = input()
print("Hello!," + name,",What a fantastic name!")

#Transition to the next scene
print("So " + name,",Tell me a little bit about yourself!")
backstory = input()
print("My oh my! You are quite the interesting figure!")

#A Riddle By Merlin the Wise
riddleList = ["Yes", "No"]
print("Now listen here dearest adventurer, for I have a riddle for you")
print("This riddle is difficult for seldom few know, answer this riddle with a simple Yes or No!")
print("Now listen here all far and wide, for I am the greatest wizard of all! Do you Deny?")

x = input()

if x == "No":
    print("Perfect answer!, Though you are too clever to be left alive!")

elif x == "Yes":
    print("What! How dare you!")

else:
    print("You have failed the riddle! For this You shall be forever turned into a fiddle!")

#Battle Time!
print("You have entered a battle with the great Merlin the Wise!")
print("Quickly! What do you do! ")
input("A. Strike with Your Sword! B. Draw your Bow and Fire! C. Cast a spell towards the Wizard!")

#Types of Attacks if statements
x = input()

if x == "A":
    print("You draw your sword and strike the Wizard!")

elif x == "B":
    print("Your arrow pierces the wind and connects with the Wizard!")

else:
    print("Your spell connects with the Wizard! Scorching his robes!")

#attack damage and randomizer

import random

attackList = [6,12,24]

x = (random.choice(attackList))

print(x)

if x == 12:
    print("Crit!")

elif x > 12:
    print("Super Crit!")

else:
    print("Hit!")

#second round of attacks
print("The Wizard is relentless and won't admit defeat! Quickly one more strike should do it!")

input("A. Slash the Wizards Heart! B. Draw your bow and Pierce the Wizards Chest! C. Annihilate him with your spell!")

x = input()

if x == "A":
    print("Your sword strikes Merlin down! I have been bested! He States!")

elif x == "B":
    print("A whistle splits the sky as your arrow plummets into his chest! My Spells weren't enough! He Says!")

else:
    print("Your spell connects with the Wizard! He turns into a pile of ash in front of you!")
"""


import random

def roulette_wheel():
    """Roulette is being played"""

money = 100

while money > 0:
    print("Here is your current money pool", + money)
    yourBet = int(input("Please enter the amount of money you would like to bet"))
    if yourBet > money:
        print("Sorry! You do not have the funds to bet this amount!")

typeBet = input("Choose how you would like to bet (number, red/black, odd/even): ")
if typeBet == "number":
    number = int(input("Please select a number between (1-36): "))
    if number < 0 or number > 36:
        print("Invalid bet")
    elif typeBet not in ["red", "black", "odd", "even"]:
        print("Invalid bet")

        winning_number = random.randint(0, 36)
        print(f"The winning number is: {winning_number}")

        if typeBet == "number":
            if number == winning_number:
                money += yourBet * 35
                print("You win!")
            else:
                money -= yourBet
                print("You lose!")
        elif typeBet == "red":
            if winning_number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
                money += yourBet
                print("You win!")
            else:
                money -= yourBet
                print("You lose!")
        elif typeBet == "black":
            if winning_number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
                money += yourBet
                print("You win!")
            else:
                money -= yourBet
                print("You lose!")
        elif typeBet == "odd":
            if winning_number % 2 == 1:
                money += yourBet
                print("You win!")
            else:
                money -= yourBet
                print("You lose!")
        elif typeBet == "even":
            if winning_number % 2 == 0:
                money += yourBet
                print("You win!")
            else:
                money -= yourBet
                print("You lose!")

        print("You ran out of money!")

