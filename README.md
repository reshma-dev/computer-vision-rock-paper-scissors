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

