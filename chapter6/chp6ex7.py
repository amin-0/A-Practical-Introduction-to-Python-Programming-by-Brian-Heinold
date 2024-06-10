'''
Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. 
A palindrome is a word that reads the same backwards as forwards.
'''
text = input('Enter string: ') # Get user's input
reverse_text = text[::-1] # Save the reversed text in a variable
if (text == reverse_text): # Check if the text is the same as the reversed and print the result
    print("The string is a palindrome")
else:
    print('The string is not a palindrome')