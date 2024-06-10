'''
Write a program that asks the user to enter a word and then capitalizes every other letter of that word. 
So if the user enters rhinoceros, the program should print rHiNoCeRoS.
'''

text = input('Enter word: ') # Get user's input
new_word = '' # Initialise a vaiable to store the new word
for i in range(len(text)): # A loop that will run for the length of the word
    if i%2 == 0: # based on the index, capitalise the letter  or leave it and add it to the new_word
        new_word = new_word + text[i]
    else:
        new_word = new_word + text[i].upper()
print(new_word)