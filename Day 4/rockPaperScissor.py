# so what we need to do first is we need to print the rules for the game

import random
print("Winning rules of the game ROCK PAPER SCISSORS are :\n" "Rock vs Paper -> Paper wins \n" "Rock vs Scissors -> Rock wins \n" "Paper vs Scissors -> Scissor wins \n")

# take input from the user
# check if the input is invalid
# convert user input to input name and then print computer is taking turn and then print computer's choice
# generate computer's choice using random module

userInput=int(input(""
                    "1 for Rock \n"
                    "2 for Paper \n"
                    "3 for Scissors \n"
                      "Please Enter Your Input Here \n"))
while userInput<1 or userInput>3 :
    print("Invalid input")
    userInput=int(input(""
                    "1 for Rock \n"
                    "2 for Paper \n"
                    "3 for Scissors \n"
                      "Please Enter Your Input Here \n"))
if userInput==1:
    print("You chose Rock, Now it's Computer's Turn...")
elif userInput==2:
    print("You chose Paper, Now it's Computer's Turn...")
elif userInput==3:
    print("You chose Scissors, Now it's Computer's Turn...")

compInput=random.randint(1,3)
if compInput==1:
    print("Computer chose Rock")
elif compInput==2:
    print("Computer chose Paper")
elif compInput==3:
    print("Computer chose Scissors")


if compInput==userInput:
    print(" It's a Draw")
elif compInput==1 and userInput==2:
    print("Congrats! YOU WIN")
elif compInput==1 and userInput==3:
    print("Ooops! You lost")
elif compInput==2 and userInput==1:
    print("Ooops! You lost")
elif compInput==2 and userInput==3:
    print("Congrats! YOU WIN")
elif compInput==3 and userInput==1:
    print("Congrats! YOU WIN")
    
elif compInput==3 and userInput==2:
    print("Ooops! You lost")


