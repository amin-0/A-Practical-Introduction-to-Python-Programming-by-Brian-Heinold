'''
Write a program that asks the user for two numbers 
and prints Close if the numbers are within .001 of each other and Not close otherwise.
'''

# GEt user's inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Calculate the difference between them
diff = abs(num1 - num2)

# Check if they are within 0.001 of each other
if diff <= 0.001:
    print('Close')
else:
    print('Not close')