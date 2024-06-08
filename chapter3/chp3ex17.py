'''
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. 
Ask the user to enter a year, and, using the // operator, determine how many leap years there have been between 1600 and that year.
'''

# Get user's input 
year = int(input('Enter year: '))

# Initialise the count
count = 0

# Loop from 1600 to date counting years that are multiples of 4
for i in range(1600, year+1, 4):
    count = count + 1
    x = i

    # If year is not a leap year, remove 1 from count
    if (i%100 == 0) and (i%400 != 0):
        count = count - 1
        print(i)
    
print(count)
