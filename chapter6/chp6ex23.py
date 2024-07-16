'''
A more general version of the above technique is the rail fence cipher, where instead of breaking things into evens and odds, 
they are broken up by threes, fours or something larger. For instance, in the case of threes, 
the string secret message would be broken into three groups. The first group is sr sg, the characters at indices 0, 3, 6, 9 and 12. 
The second group is eemse, the characters at indices 1, 4, 7, 10, and 13. The last group is ctea, the characters at indices 2, 5, 8, and 11. 
The encrypted message is sr sgeemsectea.

Write a program the asks the user for a string and uses the rail fence cipher in the threes case to encrypt the string.
Write a decryption program for the threes case.
Write a program that asks the user for a string, and an integer determining whether to break things up by threes, fours, or whatever. Encrypt the string using the rail-fence cipher.
Write a decryption program for the general case.
'''
# To encrypt
# get user's input
text = input('Enter word to be encrypted: ')
key = int(input('Enter key: '))
text_list = list(text)
fence = [[None] * len(text_list) for n in range(key)] # Create a list of list, that will contain the decrypted characters
rails = range(key)

for i,x in enumerate(text_list):
    fence[rails[i % len(rails)]][i] = x #Fill the fence with the characters
encrpty_list = [c for rail in fence for c in rail if c is not None] #rearrrange the list of list to one list, ignoring None

encrypted_word = ''.join(encrpty_list) #Join the list to form the encrypted string
print(encrypted_word)

# To decrypt
#Get user's input
text_decrypt = input('Enter word to be decrypted: ')
# text_len = range(len(text_decrypt))
key_decrypt = int(input('Enter key to decrypt: '))
text_char_pos = list(range(len(text_decrypt))) # Create a list of the index of the characters in the text
# Encrypt the list of index as done above
fence_decrypt = [[None] * len(text_char_pos) for n in range(key_decrypt)]
rails_decrypt = range(key_decrypt)
for i, x in enumerate(text_char_pos):
    fence_decrypt[rails_decrypt[i % len(rails_decrypt)]][i] = x
decrypted_list = [c for rail_decrypt in fence_decrypt for c in rail_decrypt if c is not None]
# join the characters using the 'encrypted' list of index
decrypted_word = ''.join(text_decrypt[decrypted_list.index(n)] for n in text_char_pos)
print(decrypted_word)


