'''
Write a program that asks the user to enter a length in centimeters. I
f the user enters a negative length, the program should tell the user that the entry is invalid. 
Otherwise, the program should convert the length to inches and print out the result. 
There are 2.54 centimeters in an inch.
'''
# Get user's input
len_cm = float(input('Enter length in cm: '))

# Chec if length is negative
if (len_cm < 0):
    print('Invalid entry')
else:

    # Calculate length in cm and round it to 2 decimal place
    len_inch = round(len_cm / 2.54, 2)
    print(f"{len_cm} cm equals {len_inch} inches")