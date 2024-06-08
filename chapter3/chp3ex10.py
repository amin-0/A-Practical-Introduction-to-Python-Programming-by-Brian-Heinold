'''
a. One way to find out the last digit of a number is to mod the number by 10. 
Write a program that asks the user to enter a power. Then find the last digit of 2 raised to that power.

b. One way to find out the last two digits of a number is to mod the number by 100. 
Write a program that asks the user to enter a power. Then find the last two digits of 2 raised to that power.

c. Write a program that asks the user to enter a power and how many digits they want. 
Find the last that many digits of 2 raised to the power the user entered.
'''

# Get user's input
power = int(input('Enter power: '))
digits = int(input('Enter number of digits: '))

# find the last digit of 2 raised to that power
print((2 ** power) % 10)

# find the last two digits of 2 raised to that power
print((2 ** power) % 100)

# Find the last that many digits of 2 raised to the power the user entered
print((2 ** power) % 10 ** digits)