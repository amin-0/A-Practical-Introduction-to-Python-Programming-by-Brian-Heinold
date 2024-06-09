'''
Write a program that lets the user play Rock-Paper-Scissors against the computer. 
There should be five rounds, and after those five rounds, 
your program should print out who won and lost or that there is a tie.
'''
# Import modules
from random import randint
# Variables to store the scores
computer_win = 0
human_win = 0
# Run the game for 5 rounds
for i in range(5):
    # Pick an option at random
    computer = randint(1,3)
    if computer == 1:
        computer_guess = 'R'
    elif computer == 2:
        computer_guess = 'P'
    else:
        computer_guess = 'S'
    # Get user's input
    human = input('Enter R or P or S: ')
    # Print plays 
    print(f'Computer: {computer_guess}, Human {human}')
    
    # Determine the winner and record the score
    if (computer_guess == 'R' and human == 'S'):
        computer_win = computer_win + 1
    elif (computer_guess == 'P' and human == 'R'):
        computer_win = computer_win + 1
    elif (computer_guess == 'S' and human == 'p'):
        computer_win = computer_win + 1
    elif (human == 'R' and computer_guess == 'S'):
        human_win = human_win + 1
    elif (human == 'P' and computer_guess == 'R'):
        human_win = human_win + 1
    elif (human == 'S' and computer_guess == 'P'):
        human_win = human_win + 1

# Print out the winner
if (computer_win > human_win):
    print('Computer Wins!')
elif (human_win > computer_win):
    print('Human Wins!')
else:
    print("It's a Tie!")
