import random

user_choice = input("Do you want rock, paper or scissors? ")
computer_choice = random.choice (["paper", "rock", "scissors"])
print("Computer choice: " + computer_choice)

if computer_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print("YOU WIN")
elif user_choice == "paper" and computer_choice == "rock":
    print("YOU WIN")
elif user_choice == "scissors" and computer_choice == "paper":
    print("YOU WIN")
else:
    print("YOU LOSE")