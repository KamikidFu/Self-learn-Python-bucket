import random

restart="Y"

while(restart=="Y" or restart=="y"):
    temp = input("Hello there, would you like to input a number between 0 to 9 inclusively to guess what your computer is thinking about?\n")
    guess = random.randint(0,9)
    if int(temp)==guess:
        print("Yes, you are right!")
    else:
        print("No, Computer is thinking about "+str(guess))
    restart = input("Would you like to play again? Y/N\n")

print("Game quit...")
