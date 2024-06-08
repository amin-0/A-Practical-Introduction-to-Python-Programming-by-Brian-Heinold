'''
Write a program that asks the user to enter three numbers (use three separate input statements). 
Create variables called total and average that hold the sum and average of the three numbers and 
print out the values of total and average.
'''

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
total = num1 + num2 + num3
average = total / 3
print("Total is ", total)
print("Average is ", average)