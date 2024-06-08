'''
Write a program that asks the user for their name and how many times to print it. 
The program should print out the user's name the specified number of times.
'''

name = input('Enter name: ')
num = int(input('Number of repetitions: '))

for i in range(num):
    print(name)