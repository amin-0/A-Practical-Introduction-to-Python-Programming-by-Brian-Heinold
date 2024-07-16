'''
An anagram of a word is a word that is created by rearranging the letters of the original. 
For instance, two anagrams of idle are deli and lied. 
Finding anagrams that are real words is beyond our reach until the chapter on text files. 
Instead, write a program that asks the user for a string and returns a random anagram of the string—in other words, 
a random rearrangement of the letters of that string.
'''
from random import choice

# GEt user's input
word = input('Enter word: ')
# Initialise the anagram
anagram = ''
# Create a list containing the index of the letters
letters_index = list(range(len(word)))

# Loop
for i in range(len(word)):
    # Select a random index
    letter_index = choice(letters_index)
    # remove the index from the list of indices
    letters_index.remove(letter_index)
    # Join the letters at the random index to form the anagram
    anagram = anagram + word[letter_index]
print(anagram)
