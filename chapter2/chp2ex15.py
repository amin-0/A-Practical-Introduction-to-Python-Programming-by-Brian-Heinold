'''
Write a program that prints a giant letter A like the one below. 
Allow the user to specify how large the letter should be.
    *
   * *
  *****
 *     *
*       *
'''

# Get user's input. The height must be an odd number
height = int(input('Enter size of A, enter an odd number: '))

# Calculate the width of the A
width = height + (2 * (height // 2))

# Calculate the distance to the middle of the width
mid = int((width - 1)/2)

# Calculate the distance to the middle of the height
center = int((height-1)/2)

# Print the frist row wth the * at the middle of the width
print(' '* mid + '*' + ' '* mid)

# Print the rows before the center row
for i in range(1, center):
    print(' '* (mid - i) + '*' + ' '* ((2*i)-1) + '*' + ' '*(mid - i))

# Print the center row
print(' '* center + '*'*height + ' '*center)

# Print the rows below the center row
for i in range(center,0,-1):
    print(' '* (i - 1) + '*' + ' '* (width-(2*i)) + '*' + ' '* (i - 1))

