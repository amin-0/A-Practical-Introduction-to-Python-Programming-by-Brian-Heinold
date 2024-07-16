'''
Write a program that asks the user for a large integer and inserts commas into it according to the 
standard American convention for commas in large numbers. For instance, if the user enters 1000000, 
the output should be 1,000,000.
'''
#Get user input
text = input('Enter a number: ')
# Initialise the formatted number
number = ""
#initialise a variable to count the number of digits
count = 1
for i in range(len(text)-1, -1, -1): # Loop through the text from the last number to teh first
    if count % 3 == 0: 
      number = number + text[i] + ',' # After the third digits, join the digit and a comma to the number variable
    else:
      number = number + text[i] # join the digits to the number variable
    count = count + 1
   
#Print the number variable in the reversed order
print(number[::-1])

# Alternative way
# num_userenter = int(input("Enter number: "))
# print('{:,}'.format(num_userenter))