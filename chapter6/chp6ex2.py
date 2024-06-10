'''
A simple way to estimate the number of words in a string is to count the number of spaces in the string. 
Write a program that asks the user for a string and returns an estimate of how many words are in the string.
'''

text = input('Enter a sentence: ') # Get user's input
space = text.count(' ') # Count number of spaces
words = space + 1 
print(f'The number of words in the string is {words}')