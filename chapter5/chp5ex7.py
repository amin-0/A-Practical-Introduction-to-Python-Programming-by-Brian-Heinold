'''
An integer is called squarefree if it is not divisible by any perfect squares other than 1. 
For instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those numbers (except 1) is a perfect square. 
On the other hand, 45 is not squarefree because it is divisible by 9, which is a perfect square. 
Write a program that asks the user for an integer and tells them if it is squarefree or not.
'''
# import module
from math import sqrt
# GEt user input
num = int(input('Enter number: '))
# Create a flag to check if it's squarefree or not
flag = 0
# Loop through from 2 t the num
for i in range(2, num+1):
    # If a factor of the number has a square root that is a whole number, flag it
    if (num % i == 0 and sqrt(i) % 1 == 0):
        flag = 1

# print status
if flag == 1:
    print("Not squarefree")
else:
    print("Squarefree")
