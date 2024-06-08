'''
Write a program that draws “modular rectangles” like the ones below. 
The user specifies the width and height of the rectangle, and the entries start at 0 and increase 
typewriter fashion from left to right and top to bottom, but are all done mod 10. 
Below are examples of a 3 × 5 rectangle and a 4 × 8.
0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1
'''

# Get user's input
width = int(input('Enter Width: '))
height = int(input('Enter Height: '))

number = 0

for i in range(height):
    for i in range(width):
        print(number % 10, end="")
        number = number + 1
    print("")
