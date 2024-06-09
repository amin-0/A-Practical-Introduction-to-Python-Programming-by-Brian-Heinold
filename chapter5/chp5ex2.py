'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 4 and how many end in a 9.
'''

# Create a counter
count_4 = 0
count_9 = 0
for i in range(1,100):
    x = i * i
    # Check if the square ends with 4
    if (x%10 == 4):
        count_4 = count_4 + 1
    # Check if the square enfd with 9
    elif (x%10 == 9):
        count_9 = count_9 + 1
print(f'Number of squares that end with 4 is {count_4}')
print(f'Number of squares that end with 9 is {count_9}')