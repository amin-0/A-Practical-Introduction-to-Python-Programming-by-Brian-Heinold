'''
Write a program that swaps the values of three variables x, y, and z, so that x gets the value of y, 
y gets the value of z, and z gets the value of x.
'''

# Store values in variables x,y,z
x,y,z = 5,9,2
print(f"x: {x}, y: {y}, z: {z}")

#Swap and print the values of the variables
x,y,z = y,z,x
print(f"x: {x}, y: {y}, z: {z}")