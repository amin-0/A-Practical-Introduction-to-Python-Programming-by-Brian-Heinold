'''
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. 
Your program should convert the temperature to the other unit. 
The conversions are F=9/5*C+32 and C=5/9*(F-32).
'''
# Get user's input
temp = float(input('Enter Temperature: '))
unit = input('Enter unit - C or F : ')

# Convert to the other unit and print result
if (unit == 'C' or unit == 'c'):
    f = (9/5)*temp + 32
    print(f)
elif (unit == 'F' or unit == 'f'):
    c = (5/9)*(temp - 32)
    print(c)
else:
    print('Invalid unit')
