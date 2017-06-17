#Using Pythong 3.6.1 on Windows 7
#Kamikid, 17/Jun/17
#More about random module is at https://docs.python.org/3.6/library/random.html#random.random

import random   #Import random module for generating random number

restart="Y"     #Variable of restart game command

while(restart=="Y" or restart=="y"):    #Only test if the restart is Y or y to run the game
    temp = input("Hello there, would you like to input a number between 0 to 9 inclusively to guess what your computer is thinking about?\n")
    guess = random.randint(0,9)         #Pick up a random integer by randint method
    if int(temp)==guess:                #Check the two number, using int() to parse str to int
        print("Yes, you are right!")
    else:
        print("No, Computer is thinking about "+str(guess))#Use str() to parse int to str
    restart = input("Would you like to play again? Y/N\n")

print("Game quit...")
