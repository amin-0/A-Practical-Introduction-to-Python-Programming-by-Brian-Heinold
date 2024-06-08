'''
Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.
'''
# import moduules
from math import pi, sin

# Get user's input
degree = int(input('Enter angle in degree: '))

# Calculate the anser in radian
radian = degree * pi / 180

# Print result
print(f"sin({degree}) = {round(sin(radian), 4)}")