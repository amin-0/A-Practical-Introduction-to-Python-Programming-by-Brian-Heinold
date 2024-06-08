'''
Write a program that asks the user to enter an angle between -180° and 180°. 
Using an expression with the modulo operator, convert the angle to its equivalent between 0° and 360°.
'''

# Get user's input
angle = float(input('Enter an angle between -180 and 180: '))

# Calculatte the correct angle
correct_angle = angle % 180
print(correct_angle)