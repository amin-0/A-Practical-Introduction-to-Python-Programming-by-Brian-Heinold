'''
Write a program that asks the user to guess a random number between 1 and 10. 
If they guess right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. 
Give the user five numbers to guess and print their score after all the guessing is done.
'''

# Import modules
from random import randint

# Initialise score as zero
score = 0

# Give the user five numbers
for i in range(5):
    num = randint(1,10) #Generate a random number
    guess = int(input('Enter a number between from 1 to 10: ')) # Get user's guess

    # score the user if guess is correct or not
    if (num == guess):
        score = score + 10
    else:
        score = score - 1
print(f'Your score: {score}')
