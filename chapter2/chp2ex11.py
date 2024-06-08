'''
Use a for loop to print a box like the one below. Allow the user to specify how wide and how high the box should be.
*******************
*                 *
*                 *
*******************
'''

# GEt user's input
width = int(input('Enter box width greater than 2: '))
height = int(input('Enter box height greater than 2: '))

# Print the top
print('*' * width)

# Print the middle with the spaces
for i in range(height - 2):
    print('*',' ' * (width - 2), '*', sep='')

# Print the bottom
print('*' * width)