'''
People often forget closing parentheses when entering formulas. 
Write a program that asks the user to enter a formula 
and prints out whether the formula has the same number of opening and closing parentheses.
'''
text = input('Erite a formula with parenthesis: ') # Get user's input

open = text.count('(') # Count number of open brackets
close = text.count(')') # Count number of close brackets

# Check if the brackets are equal or not and print the result
if open == close:
    print("Equal open and close brackets")
else:
    print("Unequal open and close brackets")