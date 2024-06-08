'''
A lot of cell phones have tip calculators. Write one. 
Ask the user for the price of the meal and the percent tip they want to leave. 
Then print both the tip amount and the total bill with the tip included.
'''

price = float(input("Enter meal price: "))
tip = float(input("Enter percent tip: "))
tip_amount = price * tip / 100
print("Tip amount: ", tip_amount)
print("Total bill: ", price + tip_amount)