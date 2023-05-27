import random

def get_computer_choice():
    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)
    return computer_choice

def get_user_choice():
    while True:
        user_choice = input("Your choice (rock, paper, scissors): ")
        rps_list = ["rock", "paper", "scissors"]
        if user_choice in rps_list:
            break 
        else:
            print("Invalid input, please try again")
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a tie!")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You lost")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won!")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost")
    

def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

play()