#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: HW16

import random

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

def rock_paper_scissors():
   playerhand = int(input("pick a number 1-3 rock is 1, 2 is paper, 3 is scissors."))
   opponenthand = random.randint(1, 3)
   if playerhand == 1 and opponenthand == 3:
       print("player picked rock, opponent picked scissors, player wins")
   elif playerhand == 1 and opponenthand == 2:
       print("player picked rock, opponent picked paper, opponent wins")
   elif playerhand == 1 and opponenthand == 1:
       print("player picked rock, opponent picked rock, a draw")

   elif playerhand == 2 and opponenthand == 3:
       print("player picked paper, opponent picked scissors, opponent wins")
   elif playerhand == 2 and opponenthand == 2:
       print("player picked paper, opponent picked paper, a draw")
   elif playerhand == 2 and opponenthand == 1:
       print("player picked paper, opponent picked rock, player wins")

   elif playerhand == 3 and opponenthand == 3:
       print("player picked scissors, opponent picked scissors, a draw")
   elif playerhand == 3 and opponenthand == 2:
       print("player picked scissors, opponent picked paper, player wins")
   elif playerhand == 3 and opponenthand == 1:
       print("player picked scissors, opponent picked rock, opponent wins")

   repeat_game()



def repeat_game():
    replayInput = input("Would you like to play again? Y/N ")
    if replayInput == "Y":
        rock_paper_scissors()
    else:
        exit()




rock_paper_scissors()

