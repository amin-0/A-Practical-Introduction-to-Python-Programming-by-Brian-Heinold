'''
Ask the user to enter 10 test scores. Write a program to do the following:
Print out the highest and lowest scores.
Print out the average of the scores.
Print out the second largest score.
If any of the scores is greater than 100, then after all the scores have been entered, 
print a message warning the user that a value over 100 has been entered.
Drop the two lowest scores and print out the average of the rest of them.
'''
score = float(input(f'Enter test score 1: '))

# initialise all the variables with the first score
highest = score
second_highest = score
lowest = score
second_lowest = score
greater_than_100 = False
sum = 0

# The loop runs 9 extra times and gets the right values for the variables
for i in range(2,11):
    score = float(input(f'Enter test score {i}: '))
    sum = sum + score
    if score > 100:
        greater_than_100 = True

    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest:
        second_highest = score
    elif score < lowest:
        second_lowest = lowest
        lowest = score
    elif score < second_lowest:
        second_lowest = score
        
print(f"Highest score: {highest} and lowest score: {lowest}")
print(f"The average score is {sum/10}")
print(f"The second largest score is {second_highest}")
if greater_than_100:
    print('Warning! A value larger than 100 was entered')
print(f'AVerage of top 8 numbers is {(sum - second_lowest - lowest) / 8}')