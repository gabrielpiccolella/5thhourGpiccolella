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

starterdex = {
    "Chikorita" : {
        "HP" : 45,
        "Att" : 49,
        "Def" : 65,
        "S.Att": 49,
        "S.Def": 65,
        "Spd" : 45,
        "Type" : "Grass",
        "Moves": ["Tackle", "Vine Whip"]
},
    "Cyndaquil": {
        "HP": 39,
        "Att": 52,
        "Def": 43,
        "S.Att": 60,
        "S.Def": 50,
        "Spd": 65,
        "Type": "Fire",
        "Moves": ["Tackle", "Ember"]
},
    "Totodile": {
        "HP": 50,
        "Att": 65,
        "Def": 64,
        "S.Att": 44,
        "S.Def": 48,
        "Spd": 43,
        "Type": "Water",
        "Moves": ["Tackle", "Water Gun"]
},

}

moves = {
    "Tackle": {
        "Damage": 40,
        "Type": "Normal",
        "Accuracy": 100,
        "Effect": "None",
    },
    "Vine Whip": {
        "Damage": 45,
        "Type": "Grass",
        "Accuracy": 100,
        "Effect": "None",
    },
    "Ember": {
        "Damage": 40,
        "Type": "Fire",
        "Accuracy": 100,
        "Effect": "Burn",
    },
    "Water Gun": {
        "Damage": 40,
        "Type": "Water",
        "Accuracy": 100,
        "Effect": "None",
    },
}






































