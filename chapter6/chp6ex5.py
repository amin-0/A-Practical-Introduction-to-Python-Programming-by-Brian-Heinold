'''
Write a program that asks the user to enter a string. 
The program should create a new string called new_string from the user's string such that the second 
character is changed to an asterisk and three exclamation points are attached to the end of the string. 
Finally, print new_string. Typical output is shown below:
Enter your string: Qbert
Q*ert!!!
'''

text = input('Enter word: ') # Get user's input
new_string = text[0] + '*' + text[2:] + '!!!' #Change the second letter to * and add !!! to the end
print(new_string)