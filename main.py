from random import randint
import tkinter
Stop = False
choice = ["rock", "paper", "scissors"]
uRound = 0

# scores
computerScore = 0
userScore = 0

while not Stop:

    print("Welcome to the rock, paper, scissors game!\n")
    userRound = int(input("How many rounds do you want? 1, 5 or 10"))

    while userRound > uRound:
        computer = choice[randint(0, 2)]
        print("")
        print("Please enter a choice")
        player = input(">>>").lower()
        print("Computer Chose: " + computer)

        if player == computer:
            print("Draw")
            uRound = uRound+1
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
