'''
Write a program that asks the user to enter a string, 
then prints out each letter of the string doubled and on a separate line. 
For instance, if the user entered HEY, the output would be
HH
EE
YY
'''

text = input('Enter a string: ') # Get user input
for c in text: # Loop through all the characters in the string
    print(c*2) # Print the character double 