'''
A simple way of encrypting a message is to rearrange its characters. 
One way to rearrange the characters is to pick out the characters at even indices, 
put them first in the encrypted string, and follow them by the odd characters. 
For example, the string message would be encrypted as msaeesg because the even characters are m, s, a, e 
(at indices 0, 2, 4, and 6) and the odd characters are e, s, g (at indices 1, 3, and 5).

Write a program that asks the user for a string and uses this method to encrypt the string.
Write a program that decrypts a string that was encrypted with this method.
'''
# Get user's input
word = input('Enter word to encrypt: ')

#Initiate variable to store the even and odd chars
odd_char = ''
even_char = ''

# Loop through and store the characters based o their index, then join to form the encrypted word
for i in range(len(word)):
    if i % 2 == 0:
        even_char = even_char + word[i]
    else:
        odd_char = odd_char + word[i]
encrypt_word = even_char + odd_char
print(encrypt_word)

# Get user's input on what to ecrypt
text = input('Enter word to decrypt: ')
n = len(text)

#Consider if the length of even and odd indexes are equal
if n % 2 == 1:
    mid_point = int((n+1)/2)
    even_text = text[:mid_point]
    odd_text = text[mid_point:]
else:
    mid_point = int(n/2)
    even_text = text[:mid_point]
    odd_text = text[mid_point:]
decrypt_text = '' #Initialise the decrypted word
for j in range(len(odd_text)): # loop through and decrypt the word based on the index
    decrypt_text = decrypt_text + even_text[j] + odd_text[j]
if len(even_text) != len(odd_text): # If the length of oddd and even indexes are not the same, add the last letter in even text
    decrypt_text = decrypt_text + even_text[-1]

print(decrypt_text)