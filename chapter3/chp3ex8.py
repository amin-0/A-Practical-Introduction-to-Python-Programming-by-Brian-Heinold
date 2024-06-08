'''
Write a program that asks the user for a number of seconds and prints out how many minutes and seconds that is. 
For instance, 200 seconds is 3 minutes and 20 seconds. 
[Hint: Use the // operator to get minutes and the % operator to get seconds.]

'''

# Get user's input
seconds = int(input('How many seconds: '))

# Calculate number of minutes
minutes = seconds // 60

# calculate number of extra seconds
ex_seconds = seconds % 60
print(f"{seconds} seconds is {minutes} minutes and {ex_seconds} seconds")
