'''
Write a program that given an amount of change less than $1.00 
will print out exactly how many quarters, dimes, nickels, and pennies will be needed 
to efficiently make that change. [Hint: the // operator may be useful.]
'''

# Get user's input
amount = float(input('Enter amount in cents: '))

# Calculate number of quarters and the remander
quarter = amount // 25
remainder = amount % 25

# Calculate number of dimes and remainder
dime = remainder // 10
remainder = remainder % 10

# calculate number of nickel and the remainder
nickel = remainder // 5
remainder = remainder % 5

# Calculate number of pence
pence = remainder // 1

# Print result
print(f"Change: {quarter} quarter, {dime} dime, {nickel} nickel and {pence} pence")
