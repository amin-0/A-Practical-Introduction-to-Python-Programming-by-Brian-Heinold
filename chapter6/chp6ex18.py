'''
The goal of this exercise is to see if you can mimic the behavior of the in operator 
and the count and index methods using only variables, for loops, and if statements.
1. Without using the in operator, write a program that asks the user for a string and a letter 
and prints out whether or not the letter appears in the string.
2. Without using the count method, write a program that asks the user for a string and a letter 
and counts how many occurrences there are of the letter in the string.
3. Without using the index method, write a program that asks the user for a string and a letter 
and prints out the index of the first occurrence of the letter in the string. 
If the letter is not in the string, the program should say so.
'''

# Get user's input
text = input('Enter a string: ')
letter = input('Enter a letter: ')

# Initialise the flag and counters
flag = False
count = 0
index = 0

# for ach letter in the text, if equal to letter, flag it and increase the counter
for c in text:
    if c == letter:
        flag = True
        count = count + 1

# iterate through the string and get the first instance of the letter
for i in range(len(text)):
    if text[i] == letter:
        index = 1
        break

# Print result if flag is true or not
if flag:
    print(f"String contains {letter}")
else:
    print(f"String does not contain {letter}")

print(f"Number of {letter}: {count}")
print(f"Index of first {letter}: {index}")