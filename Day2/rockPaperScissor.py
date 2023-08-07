import random

userWin=0
computerWin=0
tie=0

while True:
    userChoice = input("Enter your choice (rock, paper, or scissors): ")
    computer =  ["rock", "paper", "scissors"]
    computerChoice = random.choice(computer)

    print("your choice is ",userChoice," and computer choice is ",computerChoice)

    if userChoice != "rock" and userChoice != "paper" and userChoice != "scissors":
     print("please enter a valid choice")
     continue
    elif userChoice == computerChoice:
     tie+=1
     print("tie")
    elif userChoice == "rock" and computerChoice == "scissors":
     userWin+=1
     print("user win")
    elif userChoice == "scissors" and computerChoice == "paper":
     userWin+=1
     print("user win")
    elif userChoice == "paper" and computerChoice == "rock":
     userWin+=1
     print("user win")
    else:
     computerWin+=1
     print("computer win")

    print("user wins ",userWin," computer wins ",computerWin," tie ",tie)

    playAgain=input("you wanna play again yes/no : ")
    
    if playAgain == "no":
     break
    
    