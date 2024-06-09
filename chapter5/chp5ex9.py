'''
Write a program to count how many integers from 1 to 1000 are not perfect squares, 
perfect cubes, or perfect fifth powers.
'''

# Declare counter
count = 0
# Loop from 1 to 1000
for i in range(1, 1001):
    # Increase the counter
    count = count + 1
    # Reduce the counter if the number is a perfect square, cube or raised to the 5th power
    if (((i ** (1/2)) % 1) == 0) or (((i ** (1/3)) % 1) == 0) or (((i ** (1/5)) % 1) == 0):
        count = count - 1
print(count)