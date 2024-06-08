'''
Write a program that asks the user for a number and then prints out the 
sine, cosine, and tangent of that number.
'''
# import the necessary modules from math
from math import sin, cos, tan

# get user's input
number = int(input('Enter number: '))

# Print the result
print(f"sin({number}) = {sin(number)}")
print(f"cos({number}) = {cos(number)}")
print(f"tan({number}) = {tan(number)}")