import math
import random
userScore = 0
compScroe = 0 

def replayGame():
    while userScore != 10 or compScroe != 10:
        RockPaperSiser(UserInp())
    if userScore == 10:
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
        return("you chose the same as the computer")
        #RockPaperSiser(userInp())
    elif num == 1 and x == 3:
        return("The computer won beter luck next time")
    elif num == 2 and x == 1:
        return("The computer won beter luck next time")
    elif num == 3 and x == 2:
        return("The computer won beter luck next time")
    elif x == 1 and num == 3:
        return("Congrats you won!!")
    elif x == 2 and num == 1:
        return("Congrats you won!!")
    elif x == 3 and  num == 2:
        return("Congrats you won!!")

def UserInp():
    #Prints the three user options
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    #Gives prompt to user to choose one of the three choices
    userChoice = int(input("What is your choice?"))
    #Returns the users choice as an int
    return userChoice


