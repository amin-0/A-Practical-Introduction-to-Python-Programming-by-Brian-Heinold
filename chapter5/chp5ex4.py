'''
Write a program to compute the sum 1-2+3-4+…+1999-2000.
'''
# Initialise the sum
sum = 0
# Loop from 1 to 2000
for i in range(1, 2001):
    # If the number is odd, add to the sum
    if (i % 2 == 1):
        sum = sum + i

    # If the nmber is even, subtract from sum
    elif (i % 2 == 0):
        sum = sum - i
print(sum)