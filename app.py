#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


#Just a list from the movements allowed in the game
gameElements = ["Rock", "Paper", "Scissors"]

#Setting the score 
score = 0

#This function adds one extra point to the player's score

def addScore():
    global score
    score += 1

# A function that takes a random movement from the list 
def ranRobot():
    robot = random.choice(range(len(gameElements)))

    return robot

# Player's input
def selector():

    while True:

        try:

            moveSelect = int(input(""" 
                            Choose your move: 
                            \n 0. Rock 
                            \n 1. Paper 
                            \n 2. Scissors 
                            \n\n Other key will show an error and ask again \n"""))
            if (moveSelect >= 0 and moveSelect < 3):

                return moveSelect
            else:
                print ("\n Error: Please only enter the numbers allowed")
        except ValueError:
            print("\nError: Please enter a valid number")


# Function to stops the loop
def asking():
    
    ask = int(input("""Wanna play again?
                \n 1. Yes
                \n 2. No \n"""))
    
    if(ask == 1):
        main()
    elif(ask == 2):
        print("Your Score is " + str(score) + "\nThe number of rounds were: " + str(rounds))
          

# Main function 
rounds = 0

def main():

    print("""
          --------------------------------------------------------
          --------WELCOME TO ROCk, PAPER, SCISSORS GAME !---------
          --------------------------------------------------------""")
    global rounds
    rounds += 1
    robotZ = ranRobot()
    print(robotZ)


    move = selector()

    if((move == 0 and robotZ == 2) or (move == 1 and robotZ == 0) or (move == 2 and robotZ == 1)):
        print("YOU WIN :D !!! \n")
        addScore()
        asking()
    elif((move == 0 and robotZ == 1) or (move == 1 and robotZ == 2) or (move == 2 and robotZ == 0)):
        print("YOU LOSE :( \n")
        print("Your opponent chose ")
        asking()
    elif(move == robotZ):
        print("TIE !! :O \n")
        asking()



# Main Function call
if __name__ == "__main__":
    main()