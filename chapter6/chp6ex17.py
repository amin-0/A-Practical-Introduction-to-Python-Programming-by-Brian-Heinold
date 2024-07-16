'''
Write a program that generates the 26-line block of letters partially shown below. 
Use a loop containing one or two print statements.
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
...
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy
'''

letters = 'abcdefghijklmnopqrstuvwxyz'
# Loop 26 times, and print the alphabets
for i in range(26):
    print(letters[i:]+letters[:i]) # print from index to the index and from beginning to index