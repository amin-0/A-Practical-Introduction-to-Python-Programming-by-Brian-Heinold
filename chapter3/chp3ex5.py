'''
Write a program that generates 50 random numbers such that the first number is between 1 and 2, 
the second is between 1 and 3, the third is between 1 and 4, …, and the last is between 1 and 51.
'''

from random import randint
for i in range(1,51):
    # increase the range based on the iterator i
    print(randint(1, i+1))