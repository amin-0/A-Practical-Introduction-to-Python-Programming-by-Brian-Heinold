'''
A store charges $12 per item if you buy less than 10 items. 
If you buy between 10 and 99 items, the cost is $10 per item. 
If you buy 100 or more items, the cost is $7 per item. 
Write a program that asks the user how many items they are buying and prints the total cost.
'''

# Get user's input
items_count = int(input('Enter number of items: '))

# Check the conditions and calculate the correct bill for each condition
if items_count < 10:
    bill = 12 * items_count
    print(bill)
elif (10 <= items_count) and (items_count <= 99):
    bill = 10 * items_count
    print(bill)
else:
    bill = 7 * items_count
    print(bill)