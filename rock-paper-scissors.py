import math
import random

def RockPaperSiser(x):
    # we nead to have the user pick one and then the computer pick one
    num = random.randint(1,3)
    # geting the rock paper or siser
    # rock 3
    # siser 2
    # paper 1
    if num == x:
        return("you chose the same as the computer")
        RockPaperSiser(userInp())
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
    
def userInp():
    print("1. Paper")
    print("2. Scissors")
    print("3. Rock")
    userChoice = int(input("What is your choice?"))
    return userChoice



