'''
Below is described how to find the date of Easter in any year. Despite its intimidating appear- ance, 
this is not a hard problem. Note that bxc is the floor function, which for positive numbers just drops the decimal part of the number. 
For instance ⌊3.14⌋ = 3. The floor function is part of the math module.
C = century (1900s → C=19)
Y = year (all four digits)
m = (15+C-⌊C/4⌋ - ⌊(8C+13)/25⌋) mod 30
n = (4+C-⌊C/4⌋) mod 7
a = Y mod 4
b = Y mod 7
c = Y mod 19
d = (19c + m) mod 30
e = (2a+4b+6d+n) mod 7

Easter is either March (22 + d + e) or April (d + e - 9). There is an exception if d=29 and e=6. 
In this case, Easter falls one week earlier on April 19. There is another exception if d=28, e=6, and m=2,5,10,13,16,21,24, or 39. In this case, 
Easter falls one week earlier on April 18. Write a program that asks the user to enter a year and prints out the date of Easter in that year. 
(See Tattersall, Elementary Number Theory in Nine Chapters, 2nd ed., page 167)
'''
# Get user's input
year = int(input('Enter year: '))

# Calculate the variables
C = year // 100
Y = year
m = (15 + C -((C/4) // 1) - (((8*C + 13)/25) // 1)) % 30
n = (4 + C -((C/4) // 1)) % 7
a = Y % 4
b = Y % 7
c = Y % 19
d = (19*c + m) % 30
e = (2*a + 4*b + 6*d + n) % 7

#Calculate the dates in March and April
march_day = int(22 + d + e)
april_day = int(d + e - 9)

# Write all the conditions and print results
if (d == 29 and e == 6):
    print('April 19')
elif (d == 28 and e == 6 and (m in [2,5,10,13,16,21,24,39])):
    print('April 18')
elif (1 <= march_day and march_day <= 31):
    print(f"March {march_day}")
else:
    print(f"April {april_day}")