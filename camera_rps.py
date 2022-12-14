import random
import cv2
from time import time
from keras.models import load_model
import numpy as np

# TODO: Optional take it further later
# Think of one way to improve the application? For example, you can print the countdown in the webcam display, 
# or include a message like "press c to continue"? 
# Use your imagination and intuition to improve the user experience!

# Also, you can make your code much more readable by creating a class instead of creating multiple functions. 
# This is not necessary, but definitely a step that will showcase your good Python skills.

# Return the output of the Keras model
def get_prediction():
    
    # Load the model
    model = load_model('keras_model.h5')

    # CAMERA can be 0 or 1 based on default camera of your computer.
    camera = cv2.VideoCapture(0)

    # Current time in seconds since the Epoch
    current_time = time()

    # Predict based on a feed of 2 seconds
    while not time() > current_time + 1:
        # Grab the webcameras image.
        ret, image = camera.read()
        
        # Resize the raw image into (224-height,224-width) pixels.
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
        
        # Show the image in a window
        cv2.imshow('Webcam Image', image)
        
        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        # Normalize the image array
        image = (image / 127.5) - 1
        
        # Have the model predict what the current image is. Model.predict
        # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
        # it is the first label and 80% sure its the second label.
        probabilities = model.predict(image)
    
    camera.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    # Return the highest value probability label
    return probabilities

# Available valid choices
choices = ["rock", "paper", "scissors"]

# Function to randomly pick a choice 
def get_computer_choice():
    return random.choice(choices)

# Function to ask user to pick an option until they enter a valid choice
def get_user_choice():
    labels = {0:'rock', 1: 'paper', 2: 'scissors', 3: 'nothing'}
    
    while True:
        print("\n\nRock...Paper...Scissors...GO!\n\n")
        choice = labels[np.argmax(get_prediction())]
        if choice.lower() in choices:
            return choice.lower()
        else:
            print("That's not a valid choice, pick one of rock, paper or scissors]")

user_msg = "User"
computer_msg = "Computer"

# Function to choose a winner
def get_winner(computer_choice, user_choice):
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
    computer_wins = 0
    user_wins = 0
    while not ( computer_wins == 3 or user_wins == 3 ):
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()

        print("Computer choice: ", computer_choice, ", User choice: ", user_choice)
        winner = get_winner(computer_choice, user_choice)
        if winner == user_msg:
            user_wins += 1
        else:
            computer_wins += 1

        print("Winner in this round: ", winner)
    print(f"Best of 3 result: Computer won {computer_wins} times, User won {user_wins} times")
# Play the game!
play()

