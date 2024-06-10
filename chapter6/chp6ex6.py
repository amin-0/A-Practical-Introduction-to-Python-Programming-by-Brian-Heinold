'''
Write a program that asks the user to enter a string s and then converts s to lowercase, 
removes all the periods and commas from s, and prints the resulting string.
'''

s = input('Enter a string: ') # GEt user's input
new_s = s.lower().replace(',', '').replace('.','') # Change to lower and remove comma and full stops
print(new_s)