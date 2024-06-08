'''
Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/(x+y).
'''

x = int(input('x: '))
y = int(input('y: '))
z = abs(x-y)/(x+y)
print(z)