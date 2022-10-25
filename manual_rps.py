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
        choice = input("Pick your choice from rock / paper / scissors: ")
        if choice.lower() in choices:
            return choice.lower()

# Test functions
print("User choice: ", get_user_choice())
print("Computer choice: ", get_computer_choice())
