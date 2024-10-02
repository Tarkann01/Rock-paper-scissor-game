import math
import random

def RockPaperSiser(X):
    # we nead to have the user pick one and then the computer pick one
    num = math.ranint(1,3)
    # geting the rock paper or siser
    # rock 3
    # siser 2
    # paper 1
    if num == x:
        print("you chose the same as the computer")
        #RockPaperSiser(userInp())
    elif num == 1 && x == 3:
        print("The computer won beter luck next time")
    elif num == 2 && x == 1:
        print("The computer won beter luck next time")
    elif num == 3 && x == 2:
        print("The computer won beter luck next time")
    elif x == 1 && num == 3:
        print("Congrats you won!!")
    elif x == 2 && num == 1:
        print("Congrats you won!!")
    elif x == 3 &&  num == 2:
        print("Congrats you won!!")
    
def userInp():
    print("1. Paper")
    print("2. Scissors")
    print("3. Rock")
    userChoice = int(input("What is your choice?"))
    return userChoice



