#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello_world():
    print("Hello World!")

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["red","blue","yellow","green","orange"]


#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def random_bean():
    random_bean_choice = random.choice(beanBag)
    print(random_bean_choice)
    beanBag.remove(random_bean_choice)
    if beanBag:
        print("List is not empty")
        random_bean_again()
    else:
        print("List is empty ")
        exit()


#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def random_bean_again():
    replayInput = input("Would you like to play again? Y/N ")
    if replayInput == "Y":
        random_bean()
    else:
        exit()

#5. Call the #3 function at the bottom.
hello_world()
random_bean()
random_bean_again()