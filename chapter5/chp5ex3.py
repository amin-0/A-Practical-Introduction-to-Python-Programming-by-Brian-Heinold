'''
Write a program that asks the user to enter a value n, and then computes (1+1/2+1/3+…+1/n)-ln(n). 
The ln function is log in the math module.
'''
# import the log function
from math import log
# Get the user's input
num = int(input('Enter number: '))
# Create a variable to store the sum in the loop
total = 0
# Loop from 1 to user's number
for i in range(1, num+1):
    total  = total + (1/i)
# Print the final answer
print(total - log(num))
