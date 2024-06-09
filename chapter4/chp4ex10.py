'''
Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong.  The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.
'''

# Import modules
from random import randint

# Run the game ten times
for i in range(1, 11):

    # Generate random numbers and calulate the answer
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    answer = num1 * num2

    # Request for user's answer
    response = int(input(f"Question {i}: {num1} x {num2} = "))

    # Check if answer is correct and print right or wrong
    if response == answer:
        print('Right!')
    else:
        print(f"Wrong, The answer is {answer}.")