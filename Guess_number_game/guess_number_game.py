#Using Pythong 3.6.1 on Windows 7
#Kamikid, 17/Jun/17
#More about random module is at https://docs.python.org/3.6/library/random.html#random.random
#Version:1.1

import random   #Import random module for generating random number

restart="Y"     #Variable of restart game command
guess = random.randint(0,9)         #Pick up a random integer by randint method

while(restart=="Y" or restart=="y"):    #Only test if the restart is Y or y to run the game
    temp = input("Hello there, would you like to input a number between 0 to 9 inclusively to guess what your computer is thinking about?\n")
    int_temp = int(temp)
    if int_temp==guess:                #Check the two number, using int() to parse str to int
        print("Yes, you are right!")
        break
    elif int_temp > guess:
        print("The number you guessed is bigger than the computer thinks.")
    else:
        print("The number you guessed is smaller than the computer thinks.")
    restart = input("Would you like to play again? Y/N\n")

print("Game quit...")
