import random

# Available valid choices
choices = ["rock", "paper", "scissors"]
print("Choices: ",  choices)

# Function to randomly pick a choice 
def get_computer_choice():
    return random.choice(choices)

# Function to ask user to pick an option until they enter a valid choice
def get_user_choice():
    while True:
        choice = input("Pick your choice: ")
        if choice.lower() in choices:
            return choice.lower()
        else:
            print("That's not a valid choice, type either one of [ rock | paper | scissors ]")

# Function to choose a winner
def get_winner(computer_choice, user_choice):
    
    user_msg = "User"
    computer_msg = "Computer"
    winner = None

    if computer_choice == user_choice:
        print("It's a tie!")
        return winner
    
    if computer_choice == 'rock' and user_choice == 'paper':
        winner = user_msg
    elif computer_choice == 'paper' and user_choice == 'scissors':
        winner = user_msg
    elif computer_choice == 'scissors' and user_choice == 'rock':
        winner = user_msg
    else:
        winner = computer_msg

    return winner

# Function to play the rock-paper-scissors game
def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("Computer choice: ", computer_choice, ", User choice: ", user_choice)
    print("Winner: ", get_winner(computer_choice, user_choice))

# Play the game!
play()