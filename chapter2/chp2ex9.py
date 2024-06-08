'''
The Fibonacci numbers are the sequence below, where the first two numbers are 1, 
and each number thereafter is the sum of the two preceding numbers. Write a program that asks the user how many Fibonacci numbers to print and then prints that many.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
'''

# Get user input
number = int(input('How many Fibonacci numbers: '))

# Initialise the values of 2 consecutive numbers
first = 1
second = 1

if number <= 0:
    print('Invalid number, enter a positive integer')
elif number == 1:
    print(first)
else:
    for i in range(number):
        print(first)
        third = first + second
        first = second
        second = third