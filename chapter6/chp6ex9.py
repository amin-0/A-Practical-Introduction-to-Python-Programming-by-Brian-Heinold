'''
Ask the user for a number and then print the following, where the pattern ends at the number that the user enters.
1
 2
  3
   4
'''

number = int(input('Enter a number: ')) # Get user's input
for i in range(1, number+1): # Loop from 1 to number
    print(f"{' '* (i-1)}{i} ") # print spaces one less than number and the number