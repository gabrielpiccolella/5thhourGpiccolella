#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

def rps():
    playerHand = input("Choose a number between 1 and 3! 1 is rock, 2 is paper, and 3 is scissors.")
    if playerHand == 1:
       choice_name = 'Rock'
    elif playerHand == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    opponentsHand = random.randint(1,3)
    if opponentsHand == 1:
        comp_choice_name = 'Rock'
    elif opponentsHand == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print(choice_name, 'vs', comp_choice_name)

    if playerHand == opponentsHand:
        result = "DRAW"
    elif (playerHand == 1 and opponentsHand == 2) or (opponentsHand == 1 and playerHand == 2):
        result = 'Paper'
    elif (playerHand == 1 and opponentsHand == 3) or (opponentsHand == 1 and playerHand == 3):
        result = 'Rock'
    elif (playerHand == 2 and opponentsHand == 3) or (opponentsHand == 2 and playerHand == 3):
        result = 'Scissors'

    if result == "DRAW":
        print("It's a tie!")
    elif result == choice_name:
        print("User wins!")
    else:
        print("Computer wins!")




#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def playAgain():
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        exit()


rps()