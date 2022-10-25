# Computer Vision Project: Rock Paper Scissors  

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. 

Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. 

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Milestone 2: Create the computer vision system

- First step is to create a model which will be used by the program to determine if the player is showing a rock, a paper or scissors.  

- Use the image project option [here](https://teachablemachine.withgoogle.com/) to create sets of images of each option and build a model using them. We will need a 4th option to hold images that are neither of Rock / Paper / Scissors.  
  
  Create the model with 4 classes:
  - Rock
  - Paper
  - Scissors
  - Nothing  

- It is possible to test the model on teachablemachine to ensure you are happy with the results. More images the model gets trained with, more accurate will be the results.

- Download the model
  
  Download the model from the "Tensorflow" tab in Teachable-Machine. The model should be named ```keras_model.h5``` and the text file containing the labels should be named ```labels.txt```.
  
  These files contain the structure and the parameters of a deep learning model.

## Milestone 3: Install the dependencies  

Tensorflow and Keras are used to build deep learning models (neural networks). As part of this milestone, we get all dependencies installed in an environment created for this project: opencv-python, tensorflow and ipykernel

- Create an environment 'computer_vision_env' 
  ```python
  conda create -n computer_vision_env
  conda activate computer_vision_env
  conda install pip
  ```

- Get Tensorflow for Mac  
  
  Follow steps from the section that says "arm64: Apple Silicon" from [this](https://developer.apple.com/metal/tensorflow-plugin/) link to install tensorflow for Mac
  ```python
  conda install -c apple tensorflow-deps
  ```

- Install the remaining necessary dependencies
  - opencv
    ```python
    conda install -c conda-forge opencv
    ```
  - ipykernel
    ```python
    pip install ipykernel
    ```

- Create a requirements.txt file to help easily install the exact same dependencies later
  - Get list of dependencies into requirements.txt:
    ```python
    pip list > requirements.txt
    ```
  - To easily install these exact dependencies later, run
    ```python
    pip install requirements.txt
    ```

## Milestone 4: Create a Rock-Paper-Scissors game  
Create a Python script that will simulate a Rock-Paper-Scissors game: the code will ask for a choice, then compare the user's choice with a randomly chosen option by the computer and show the winner between the two  

### Store the valid choices in a list  
  ```choices = ["rock", "paper", "scissors"]```

### Functions to implement the game 
- Function to randomly pick a choice 
  ```get_computer_choice()``` - use the random module to randomly pick an option and return the choice

- Function to ask user to pick an option until they enter a valid choice
  ```get_user_choice()```

- Function to choose a winner
```get_winner(computer_choice, user_choice)``` - gets  the user and computer choices as parameters and decide who won

- Function to play the rock-paper-scissors game
```play()``` - makes use of the above function to play the game