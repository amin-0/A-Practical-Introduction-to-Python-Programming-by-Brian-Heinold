'''
In calculus, the derivative of x4 is 4x3. The derivative of x5 is 5x4. The derivative of x6 is 6x5. 
This pattern continues. Write a program that asks the user for input like x3 or x25 and prints the derivative. 
For example, if the user enters x3, the program should print out 3x2.
'''

text = input('Enter text: ') # Get user's input

power = int(text[1:]) #Get the power
print(f'The derivative of {text} is {power}x{power-1}') #Print the derivative
