'''
Write a program that asks the user to enter a string. The program should then print the following:
The total number of characters in the string
The string repeated 10 times
The first character of the string (remember that string indices start at 0)
The first three characters of the string
The last three characters of the string
The string backwards
The seventh character of the string if the string is long enough and a message otherwise
The string with its first and last characters removed
The string in all caps
The string with every a replaced with an e
The string with every letter replaced by a space
'''

# Get user's input
text = input('Enter a string: ')

# Print the answers
print(f'a. The number of characters in the string is {len(text)}')
print(f'b. {(text + ' ') * 10}')
print(f'c. The first character if the string is {text[0]}')
print(f'd. The first 3 characters of the string are {text[:3]}')
print(f'e. The last 3 characters of the string are {text[-3:]}')
print(f'f. The string backwards is {text[::-1]}')
if len(text) > 7:
    print(f'g. The seventh character of the string is {text[6]}')
else:
    print('g. String has less than 7 characters')
print(f"h. The string with it's first and lat letter removed is {text[1:-1]}")
print(f'i. Thes string in all caps is {text.upper()}')
print(f'j. The string with every a replacd with e is {text.replace('a','e')}')
print(f'k. The string with every letter replaced by a space is {text.replace(text, ' ')}')
