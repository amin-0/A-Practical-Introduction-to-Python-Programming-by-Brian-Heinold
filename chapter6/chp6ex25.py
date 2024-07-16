'''
In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or 3(x+5). 
Computers prefer those expressions to include the multiplication symbol, like 3*x+4*y or 3*(x+5). 
Write a program that asks the user for an algebraic expression and then inserts multiplication symbols where appropriate.
'''
# Get user's input
exp = input('Enter algebraic expression: ')
#Initialise new expression
new_exp = ''

for i in range(len(exp)):
    if i == (len(exp) - 1): #Cnside the edge case fr the last letter
        new_exp = new_exp + exp[i]
    elif exp[i].isnumeric() and (exp[i+1].isalpha() or exp[i+1] == '('): # if a number is followed by a letter of (, add *
        new_exp = new_exp + exp[i] + '*'
    else:
        new_exp = new_exp + exp[i] 
print(new_exp)