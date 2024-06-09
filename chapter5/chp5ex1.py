'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
'''

# Create a counter
count = 0
for i in range(1,100):
    x = i * i
    # Check if the square ends with 1
    if (x%10 == 1):
        count = count + 1
        print(x)
print(count)