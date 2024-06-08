'''
Write a program that generates a random decimal number between 1 and 10 
with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
'''

from random import uniform
# Uniform return random floats
# Approximate to  decimal points
x = round(uniform(1,10), 2)
print(x)