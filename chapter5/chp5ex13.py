'''
In the last chapter there was an exercise that asked you to create a multiplication game for kids. 
Improve your program from that exercise to keep track of the number of right and wrong answers. 
At the end of the program, print a message that varies depending on how many questions the player got right.
'''
# import modules
from random import randint

# initialise variable for the score of right and wrong answers
right = 0
wrong = 0

# run the loop 10 times
for i in range(1, 11):
    # Generate random numbers
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    answer = num1 * num2
    # REquest for answer from the user
    response = int(input(f"Question {i}: {num1} x {num2} = "))

    # Increase the counter based on if the answer is correct or wrong
    if response == answer:
        print('Right!')
        right = right + 1
    else:
        print(f"Wrong, The answer is {answer}.")
        wrong = wrong + 1
    
    # Print result
print(f'You had {right} correct answers and {wrong} wrong answers')