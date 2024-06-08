'''
Use a for loop to print a triangle like the one below. 
Allow the user to specify how high the triangle should be.
*
**
***
****
'''

# Get user's input
height = int(input('Height: '))

# Print an increasing number of stars based on the iterator i
for i in range(1, height+1):
    print('*' * i)