'''
At a certain school, student email addresses end with @student.college.edu, 
while professor email addresses end with @prof.college.edu. 
Write a program that first asks the user how many email addresses they will be entering, 
and then has the user enter those addresses. After all the email addresses are entered, 
the program should print out a message indicating either that all the addresses are student addresses or 
that there were some professor addresses entered.
'''

number = int(input('How many email addresses: ')) # Get the number of addresses
prof_flag = False # Creat a flag to now if there's a professors address. Set it o False

for i in range(number):
    address = input('Enter email address: ') # Get an email address
    if '@prof.college.edu' in address: # if it's a professor's, flag it
        prof_flag = True 
if prof_flag: # IF the flag has turned true,  print the result
    print("You entered a professor's email address")
else:
    print("All the addresses are student's addresses")