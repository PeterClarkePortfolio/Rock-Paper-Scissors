from random import randint
import tkinter
# importing modules

Stop = False

# the Stop = Fale, and while not Stop: is designed to create a loop. I am aware there are other reccomended ways of doing this. 
choice = ["rock", "paper", "scissors"]
# choice is a list of the possible options the computer can choose from.
uRound = 0
# uRound is to designed to tell the system what round the user is currently on. As default this is 0, and will increase by 1 after each match until it meets the users chosen number of rounds.

computerScore = 0
userScore = 0
drawCount = 0
# Each time the user or computer scores it will update the score varibles. At the end of the game the total scores will be shown to the user. 
# drawCount was a later additon designed to count the number of draws, it too is shown at the end of the game.

while not Stop:

    print("Welcome to the rock, paper, scissors game!\n")
    
    # basic try except code for validation 
    try:
        userRound = int(input("How many rounds do you want? 1, 5 or 10"))
    except ValueError:
        print("Please only enter whole numbers!")
        userRound = int(input("Enter a whole number"))

    while int(userRound) > uRound:
        computer = choice[randint(0, 2)]
        print("")
        print("Please enter a choice")
        player = input(">>>").lower()
        print("Computer Chose: " + computer)

        if player == computer:
            print("Draw")
            uRound = uRound+1
            drawCount = drawCount +1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "rock" and computer == "paper":
            print("Computer Wins")
            uRound = uRound + 1
            computerScore = computerScore + 1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "rock" and computer == "scissors":
            print("Player Wins")
            uRound = uRound + 1
            userScore = userScore + 1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "paper" and computer == "rock":
            print("Player Wins")
            uRound = uRound + 1
            userScore = userScore + 1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "paper" and computer == "scissors":
            print("Computer Wins")
            uRound = uRound + 1
            computerScore = computerScore + 1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "scissors" and computer == "rock":
            print("Computer Wins")
            uRound = uRound + 1
            computerScore = computerScore + 1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "scissors" and computer == "paper":
            print("Player wins\n\n")
            uRound = uRound + 1
            userScore = userScore + 1
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
        elif player == "close":
            print(f"Your Score is {userScore}\n\nThe Computer Score is {computerScore}\t")
            Stop = True
        else:
            print("Please only use rock, paper or scissors")
    else:
        print(f"The final scores are: \n\nComputer = {computerScore}\nUser = {userScore}\n")
        print(f"There were {drawCount} draws")
        print("Thank you for playing")
        uRound = 0

        # updated 4th July 2021 17:45 by Peter Clarke
