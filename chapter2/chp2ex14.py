'''
Use for loops to print a diamond like the one below. Allow the user to specify how high the diamond should be.
   *
  ***
 *****
*******
 *****
  ***
   *
'''

# Get users input, the height must be an odd number to form a diamond
height = int(input('Diamond Height, Enter an odd number: '))

# Check that height is an odd number
if (height % 2) == 0:
    print('Enter an odd number')


else:
    # Calculate the midpoint of the height
    n = (height // 2) + 1
    '''
    # Method 1
    # Print the top half of the diamond till the middle
    for i in range(1, n+1):
        print((' ' * (n-i)) + ('*' * ((i*2)-1)) + (' ' * (n-i)))
    # Print the bottom half of the diamond
    for i in range(n-1, 0, -1):
       print((' ' * (n-i)) + ('*' * ((i*2)-1)) + (' ' * (n-i)))

    '''
    # Method 2
    # A loop from th etop to bottom of the diamond
    for i in range( 1, height + 1):
        # picture a square with side, height. s is the space to each side of the diamond
        s = i - n

        # s has to be a positive value
        if s < 0:
            s = -s
        # print the diamond
        print(' ' * s + '*' * (height - s *2) + ' ' * s)
    