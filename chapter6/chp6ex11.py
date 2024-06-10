'''
Write a program that asks the user to enter a word that contains the letter a. 
The program should then print the following two lines: 
On the first line should be the part of the string up to and including the first a, 
and on the second line should be the rest of the string. Sample output is shown below:
Enter a word: buffalo
buffa
lo
'''

text = input('Enter a word that contains letter a: ') # Get user's input
index = text.index('a') # Get the position of the first a
print(text[:index+1]) # Print from the start of the work till the a
print(text[index+1:]) # Print the remaining letters