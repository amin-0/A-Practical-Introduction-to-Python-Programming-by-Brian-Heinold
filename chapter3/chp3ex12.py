'''
Write a program that asks the user for a number and prints out the factorial of that number.
'''
# Get user's input
number = int(input('Enter number: '))

# Initialise the total as the number
total = number

# Loop down to 1 and Calculate the factorial
for i in range(number-1,0,-1):
    total = total * i
print(f"The factorial of {number} is {total}")