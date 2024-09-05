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
    print("Perfect answer!, Good luck on your future adventures friend!")

elif x == "Yes":
    print("What! How dare you! ")

else:
    print("You have failed the riddle! For this You shall be forever turned into a fiddle!")




