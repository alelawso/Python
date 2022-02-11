#Rock, Paper, Scissors

#import modules
import random
import sys

#loop
while True:
    weapons =['Rock','Paper','Scissors']
    opponent = random.choice(weapons)

    prompt = input(f'\nRock, Paper or Scissors? (reply STOP to quit)')

    if prompt == "STOP":
        sys.exit()
    else:
        if opponent == prompt:
            print(f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: DRAW! Try again.")
        
        #user picks scissors
        elif opponent == "Rock":
            if prompt == "Scissors":
                print (f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: Rock beats scissors. You Lost.")
            else:
                print(f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: Paper beats rock. YOU WON!.") 
        
        #user picks rock
        elif opponent == "Paper":
            if prompt == "Rock":
                print (f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: Paper beats rock. You lost.")
            else:
                print(f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: Scissors beats paper. YOU WON!")

        #user picks rock
        elif opponent == "Scissors":
            if prompt == "Rock":
                print (f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: Rock beats scissors. YOU WON!")
            else:
                print(f"\nYou chose {prompt} \nOpponent chose {opponent} \nResult: Scissors beats paper. You lost.")

     
