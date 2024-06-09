'''
Write a program that asks the user how many credits they have taken. 
If they have taken 23 or less, print that the student is a freshman. 
If they have taken between 24 and 53, print that they are a sophomore. 
The range for juniors is 54 to 83, and for seniors it is 84 and over.
'''
# Get user's input
temp = float(input('Enter temp in Celsius: '))

# Check for the different conditions and print result
if (temp < -273.15):
    print('Temperature is invalid, it is below absolute zero')
elif (temp == -273.15):
    print('Temperature si at absolute zero')
elif (-273.15 < temp and temp < 0):
    print('Temperature is below freezing')
elif (temp == 0):
    print('Temperature is at freezing point')
elif (0 < temp and temp < 100):
    print('Temperature is in normale range')
elif (temp == 100):
    print('Temperature is at boiling point')
else:
    print('Temperature is above the boiling point')