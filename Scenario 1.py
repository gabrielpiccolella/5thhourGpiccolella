#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment:Scenario 1



# You are a programmer for a fledgling game developer. Your team lead
# has asked you to create a nested dictionary containing five enemy
# creatures (and their properties) for combat testing. Additionally,
# the testers are asking for a way to input changes to the enemy's
# damage for balancing, as well as having it print those changes to
# confirm they went through.

# It is up to you to decide what properties

# are important and the theme of the game.

#Creating Nested Dictionary
fallGuys = {
"Yellow": {
    "Type" : "Electric",
    "Speed": 80,
    "Attack": 70,
    "Hp":125,
    "Attack Effects": "Stun",
},
"Blue": {
    "Type": "Water",
    "Speed": 125,
    "Attack": 50,
    "Hp": 75,
    "Attack Effects": "Slow",
},
"Red": {
    "Type" : "Fire",
    "Speed": 100,
    "Attack": 125,
    "Hp":50,
    "Attack Effects": "Burn",
},
"White": {
    "Type": "Ice",
    "Speed": 80,
    "Attack": 60,
    "Hp": 150,
    "Attack Effects": "Freeze",
},
"Chrome": {
    "Type": "Special",
    "Speed": 200,
    "Attack": 175,
    "Hp": 50,
    "Attack Effects": "Special",
},
}

#Changes for Yellow Fall Guy
newAttackY = int(input("Enter a new Attack for Yellow: "))

fallGuys["Yellow"]["Attack"] = newAttackY

#Changes for Blue Fall Guy
newAttackB = int(input("Enter a new Attack for Blue: "))

fallGuys["Blue"]["Attack"] = newAttackB

#Changes for Red Fall Guy
newAttackR = int(input("Enter a new Attack For Red: "))

fallGuys["Red"]["Attack"] = newAttackR

#Changes for White Fall Guy
newAttackW = int(input("Enter a new Attack For White: "))

fallGuys["White"]["Attack"] = newAttackW

#Changes for Purple Fall Guy
newAttackC = int(input("Enter a new Attack For Chrome: "))

fallGuys["Chrome"]["Attack"] = newAttackC


#Printing New changes
print("Print New Changes? Yes/No")

#If Statements
x = input()

if x == "Yes":
    print("Printing Changes!")

    print("Yellow New Attack Value is")
    print(fallGuys["Yellow"]["Attack"])

    print("Blue New Attack Value is")
    print(fallGuys["Blue"]["Attack"])

    print("Red New Attack Value is")
    print(fallGuys["Red"]["Attack"])

    print("White New Attack Value is")
    print(fallGuys["White"]["Attack"])

    print("Chrome New Attack Value is")
    print(fallGuys["Chrome"]["Attack"])



elif x == "No":
    print("Okay!")

else:
    print("Error")





