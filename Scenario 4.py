#Name: Gabriel Piccolella
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

import statistics

numberOfPlayers = int(input("How many players are in the game?"))

ratings = []

for i in range(numberOfPlayers):
    rat = int(input(f"Player {i + 1} rate the current model (1 - 5) "))

    if rat < 1 or rat > 5:
        print("Error, please enter a number between 1 and 5.")
    else:
        ratings.append(rat)

if len(ratings) > 0:
    average = statistics.mean(ratings)
    print("Here are your ratings", ratings)
    print("Here is your average rating", average)
else:
    print("Invalid ratings entered")






