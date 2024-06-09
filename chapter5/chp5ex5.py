'''
Write a program that asks the user to enter a number and prints the sum of the divisors of that number. 
The sum of the divisors of a number is an important function in number theory.
'''
# Get user's input
num = eval(input('Enter a number: '))

# Initialise sum
sum = 0

# Loop from 1 to num
for i in range(1, num+1):
    # if the number is a divisor, add it to sum
    if num % i == 0:
        sum = sum + i
print(sum)