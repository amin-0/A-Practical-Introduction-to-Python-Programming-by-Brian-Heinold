'''
Write a program that asks the user to enter a weight in kilograms. 
The program should convert it to pounds, printing the answer rounded to the nearest tenth of a pound.
'''
# Get user's input
weight_kg = float(input('Enter weight in kg: '))

# Convert kg to pounds
weight_lb = round(weight_kg*2.2, 1)

# Print result
print(weight_lb)