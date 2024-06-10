'''
Write a program that asks the user to enter a word and prints out whether that word contains any vowels.
'''

text = input('Enter a word: ') # Get user's input
vowel_flag = False # Create a flag to check if there's a vowel or not
for letter in text: # Check all the letters in the text
    if letter in 'aeiou': # If letter is a vowel
        vowel_flag = True # Change the flag to true
if vowel_flag:
    print('Contains vowel')  # Print result
else:
    print('Does not contain vowel')