#Hunter Esler 8/27/2020
#Number guesser "game"

#utilizes 
#   argument integer checking with try catch
#   user input from console
#   random

#basic python learning

#Idea from https://www.upgrad.com/blog/python-projects-ideas-topics-beginners

#Usage: py numguess.py maxrange(optional)
#maxrange: must be greater than 0



import sys #arguments
import os
import random

max = 1000

#was there an input for a custom range?
args = sys.argv
try:
    if (len(args) > 1):

        if (args[1].lower() == "help"):#simple help
            print(f"Usage: py {os.path.basename(__file__)} maxrange(optional)")
            quit()

        #input checking
        num = int(args[1])
        if (num < 1):
            print("Max range must be greater than 0")
            quit()

        max = num # quit wouldnt bring us here
except ValueError:
    print("Given argument was not an integer!")
    quit()

print(f"Guess the number that is between 1-{max}!")

random.seed()
answer = random.randrange(1, max, 1) #1-max, 1 as step

tries = 0
guess = -1

#user guessing
while (guess != answer):
    try:
        guess = int(input())
    except ValueError:
        print("Please input an integer!")
        continue
    tries = tries + 1
    if (guess == answer):
        print(f"Congrats! You got the answer in {tries} guesses!")
        break # redundant but..
    elif (guess < answer):
        print("Higher . . .")
    else:
        print("Lower . . .")

