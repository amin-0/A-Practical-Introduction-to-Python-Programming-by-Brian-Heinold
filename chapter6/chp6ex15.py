'''
When I was a kid, we used to play this game called Mad Libs. 
The way it worked was a friend would ask me for some words and then insert those words into a story at specific places 
and read the story. The story would often turn out to be pretty funny with the words I had given since 
I had no idea what the story was about. The words were usually from a specific category, like a place, an 
animal, etc. For this problem you will write a Mad Libs program. First, you should make up a story and 
leave out some words of the story. Your program should ask the user to enter some words and tell them what 
types of words to enter. Then print the full story along with the inserted words. Here is a small example,
 but you should use your own (longer) example:
Enter a college class: CALCULUS
Enter an adjective: HAPPY
Enter an activity: PLAY BASKETBALL

CALCULUS class was really HAPPY today.  We learned how to
PLAY BASKETBALL today in class.  I can't wait for
tomorrow's class!
'''

name = input('Enter a name: ')
state = input('Enter a state: ')
food = input('Enter a food: ')
vehicle = input('Enter a vehicle: ')
colour = input('Enter a colour: ')

print(f"My name is {name}, I live in {state}. I love {state} because of {food} and {vehicle}. {state}'s {vehicle} are coloured {colour}.")
