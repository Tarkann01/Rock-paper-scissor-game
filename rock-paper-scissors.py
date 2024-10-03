import math
import random

userScore = 0
compScroe = 0 

def ReplayGame():
    while userScore != 10 or compScroe != 10:
        #loops till some one gets to ten wins
        RockPaperSiser(UserInp())
    if userScore == 10: 
        #looks to see if the user won else the computer won
        print("You won with a score of " + userScore + "to " + compScroe)
    else:
        print("You lost with a score of " + userScore + "to " + compScroe)

def RockPaperSiser(x):
    # we nead to have the user pick one and then the computer pick one
    user = x
    num = random.randint(1,3)
    # geting the rock paper or siser
    # rock is 3
    # siser is 2
    # paper is 1
    # num is the computer
    # x is the user
    if num == x:
        print("you chose the same as the computer")
        #RockPaperSiser(userInp())
    elif num == 1 and x == 3:
        compScore += 1
        print("The computer won beter luck next time")
    elif num == 2 and x == 1:
        compScore += 1
        print("The computer won beter luck next time")
    elif num == 3 and x == 2:
        compScore += 1
        print("The computer won beter luck next time")
    elif x == 1 and num == 3:
        userScore += 1
        print("Congrats you won!!")
    elif x == 2 and num == 1:
        userScore += 1
        print("Congrats you won!!")
    elif x == 3 and  num == 2:
        userScore += 1
        print("Congrats you won!!")
    print("User:",userScore)
    print("Computer:",compScore)

def UserInp():
    #Prints the three user options
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    #Gives prompt to user to choose one of the three choices
    userChoice = int(input("What is your choice?"))
    #Returns the users choice as an int
    return userChoice


