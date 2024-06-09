'''Generate a random number between 1 and 10. 
Ask the user to guess the number and print a message based on whether they get it right or not.
'''

# Import modules
from random import randint

# Get user's input
guess = int(input('Enter number between 0 and 10: '))

# Generate a random number
num = randint(0,10)

# Check if the user guess right or wrong
if (num == guess):
    print('You guessed right!')
else:
    print('You guessed wrong')
print(f"number: {num}, your guess: {guess}")