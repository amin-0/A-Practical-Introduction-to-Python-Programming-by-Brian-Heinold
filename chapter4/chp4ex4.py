'''
Generate a random number between 1 and 10. 
Ask the user to guess the number and print a message based on whether they get it right or not.
'''
# Get user's input
credits = int(input('Enter number of credits: '))

# Check the cnditions and print result
if (credits <= 23):
    print('Freshman!')
elif (24 <= credits and credits <= 53):
    print('Sophomore!')
elif (54 <= credits and credits <= 83):
    print('Junior!')
else:
    print('Senior!')