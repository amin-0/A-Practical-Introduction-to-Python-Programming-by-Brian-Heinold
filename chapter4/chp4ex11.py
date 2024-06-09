'''
Write a program that asks the user for an hour between 1 and 12, 
asks them to enter am or pm, and asks them how many hours into the future they want to go. 
Print out what the hour will be that many hours into the future, printing am or pm as appropriate. 
An example is shown below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm
'''

# Get user's input
hour = int(input('Enter hour: '))
period = int(input('am (1) or pm (2): '))
ahead = int(input('How many hours ahead? '))

# Calculate the new hour on a 24 hours scale
if (period == 1):
    new_time = hour + ahead
elif (period == 2):
    new_time = 12 + hour + ahead

# Convert back to a 12 hours scale
new_hour = new_time % 12

# Determine if the new hour is in am or pm
new_period = (new_time // 12)

# Edge case: if the time is a multiple of 12, then it is 12
if (new_hour == 0):
    new_hour = 12

# Save the new period if its am or pm
if (new_period % 2 == 0):
    time_period = 'am'
elif (new_period % 2 == 1):
    time_period = 'pm'

# Print the new time
print(f"New hour: {new_hour} {time_period}")