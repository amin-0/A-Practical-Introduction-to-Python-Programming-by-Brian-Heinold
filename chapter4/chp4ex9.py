'''
Write a program that asks the user to enter a number and prints out all the divisors of that number. 
[Hint: the % operator is used to tell if a number is divisible by something. See this_section.]
'''
# Get user's input
num = int(input('Enter number: '))

# Loop through 1 to the number and the divisors
for i in range(1, num+1):
    if num % i == 0:
        print(i)