# CV-Rock-Paper-Scissors
My code for a computer vision Rock Paper Scissors game

## Creating the computer vision system
- Teachable machine to create the classes: Rock, Paper, Scissors, Nothing
- Downloaded the keras.h5 model (made with the TensorFlow software library) and labels.txt file

## Environment creation
- In my terminal I created an environment using conda and pip to install these packages: opencv, tensorflow and ipykernel
- These were needed in order to use the computer vision system
- I then used a check_method.py script to test my environment works 

## Manual - Rock, Paper, Scissors script creation
- I created a script in order to play the rock paper scissors game
- I made 4 functions: get_computer_choice, get_user_choice, get_winner and play
- get_computer_choice: I used the random module and inputted a list containing elements "rock" "paper" and "scissors into the random.choice function. I assigned the result to computer_choice variable 
- get_user_choice: I used the input function so the user can input their choice. I put this is a while loop and if input was valid then loop would break otherwise it would as for another input. I then returned the user choice
- get winner: I used user choice and computer choice as parameters and then used a series of if-elif statements to print whether the user won, lost or tied the game. 
- play: I put all these functions together in order to create the full game 
