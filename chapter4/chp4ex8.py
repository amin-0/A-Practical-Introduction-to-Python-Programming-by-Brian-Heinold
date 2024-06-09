'''
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. 
Write a program that asks the user for a year and prints out whether it is a leap year or not.
'''

# Get user's input
year = int(input('Enter year: '))

# Check the conditions and print the result
if (year % 100) == 0 and (year % 400 == 0):
    print('Leap year')
elif(year % 100 == 0):
    print('Not leap year')
elif (year % 4 == 0):
    print('Leap year')
else:
    print('Not leap year')