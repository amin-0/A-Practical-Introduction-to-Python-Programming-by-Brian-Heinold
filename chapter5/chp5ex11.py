'''
Write a program that computes the factorial of a number. 
The factorial, n!, of a number n is the product of all the integers between 1 and n, including n. 
For instance, 5!=1·2·3·4·5=120. [Hint: Try using a multiplicative equivalent of the summing technique.]
'''

num = int(input('Enter a number: '))
# Initialize your number as 1 because you'll be multiplying
answer = 1

# loop from number to 1
for i in range(num,0,-1):
    answer = answer * i # multily answer by number
print(f"The factorial of {num} is {answer}") #Print answer
