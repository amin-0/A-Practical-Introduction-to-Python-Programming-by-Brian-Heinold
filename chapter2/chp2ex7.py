'''
Write a program that uses exactly four for loops to print the sequence of letters below.
AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
'''

for i in range(4):
    print('AA', end='')
print('AAB', end='')
for i in range(3):
    print('BB', end='')
for i in range(4):
    print('CD', end='')
print('E', end='')
for i in range(3):
    print('FF', end='')
print('G', end='')