'''
Write a program that asks the user to enter two strings of the same length. 
The program should then check to see if the strings are of the same length. 
If they are not, the program should print an appropriate message and exit. 
If they are of the same length, the program should alternate the characters of the two strings. 
For example, if the user enters abcde and ABCDE the program should print out AaBbCcDdEe.
'''
text1 = input('Enter first string: ') # Get user inputs
text2 = input('Enter second string: ')
new_text = '' # Initiallise a variable to store the new word

if len(text1) != len(text2): # Check if lengths are not equal and print a message
    print('Enter strings with equal lengths')
else:
    for i in range(len(text1)): # If they are equal, add each letter of text1 and tex2 to the new_text variable
        new_text = new_text + text1[i] + text2[i]
print(new_text)