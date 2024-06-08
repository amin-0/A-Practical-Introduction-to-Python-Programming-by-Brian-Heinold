'''
Use a for loop to print a box like the one below. 
Allow the user to specify how wide and how high the box should be. 
[Hint: print('*' * 10) prints ten asterisks.]
*******************
*******************
*******************
*******************

'''
# Get user's input
width = int(input('Enter box width: '))
height = int(input('Enter box height: '))

for i in range(height):
    print('*' * width)