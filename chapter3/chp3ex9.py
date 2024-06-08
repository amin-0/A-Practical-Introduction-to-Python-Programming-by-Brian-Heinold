'''
Write a program that asks the user for an hour between 1 and 12 and for how many hours in the future they want to go. Print out what the hour will be that many hours into the future. An example is shown below.
Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock
'''

# Get user's input
hour = int(input('Enter hour: '))
ahead = int(input('How many hours ahead: '))

# Calculate th enew hour
new_hour = (hour + ahead) % 12

# Edge case: 0 hour is 12
# PRint result
if new_hour == 0:
    print(f"New hour: 12 o'clock")
else:
    print(f"New hour: {new_hour} o'clock")
