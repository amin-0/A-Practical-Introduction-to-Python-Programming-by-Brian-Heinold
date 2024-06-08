'''
Use a for loop to print an upside down triangle like the one below. 
Allow the user to specify how high the triangle should be.
****
***
**
*
'''

# Get user's input
height = int(input('Height: '))

# Print a decreasing number of stars based on the iterator i
for i in range(height, 0, -1):
    print('*' * i)