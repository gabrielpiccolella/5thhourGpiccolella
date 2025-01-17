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
