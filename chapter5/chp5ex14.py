'''
This exercise is about the well-known Monty Hall problem. In the problem, you are a contestant on a game show. 
The host, Monty Hall, shows you three doors. Behind one of those doors is a prize, and behind the other two doors are goats. 
You pick a door. Monty Hall, who knows behind which door the prize lies, then opens up one of the doors that doesn't contain the prize. 
There are now two doors left, and Monty gives you the opportunity to change your choice. 
Should you keep the same door, change doors, or does it not matter?

a. Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch 
and what percentage of the time you would win by not switching.
b. Try the above but with four doors instead of three. There is still only one prize, and Monty still opens up one door and 
then gives you the opportunity to switch.
'''
from random import randint, choice
# Initialise the doors to be opened with a prze door at random

keep = 0
switch = 0
for i in range(10000):
    # The player selects a door at random
    player_door = randint(1,3)
    # The prize is behind a random door too
    win_door = randint(1,3)

    # If the prize is behind the first door, the choices are 1 and any other number
    if win_door == 1:
        if player_door == win_door:
            doors = [1, choice([2,3])]
        else:
            doors = [win_door, player_door]
        # if player keeps his guess
        player_keep = player_door
        # if player decides to switch
        doors.remove(player_door)
        player_switch = doors[0]
        #Check if initial door has the prize
        if player_keep == win_door:
            keep = keep + 1
        # Check if the switch has the prize
        elif player_switch == win_door:
            switch = switch + 1

    # If the prize is behind the second door, the choices are 2 and any other number
    if win_door == 2:
        if player_door == win_door:
            doors = [2, choice([1,3])]
        else:
            doors = [win_door, player_door]

        # if player keeps his guess
        player_keep = player_door

        # if player decides to switch
        doors.remove(player_door)
        player_switch = doors[0]

        #Check if initial door has the prize
        if player_keep == win_door:
            keep = keep + 1

        # Check if the switch has the prize
        elif player_switch == win_door:
            switch = switch + 1

    # If the prize is behind the third door, the choices are 3 and any other number
    if win_door == 3:
        if player_door == win_door:
            doors = [3, choice([1,2])]
        else:
            doors = [win_door, player_door]

        # if player keeps his guess
        player_keep = player_door

        # if player decides to switch
        doors.remove(player_door)
        player_switch = doors[0]

        #Check if initial door has the prize
        if player_keep == win_door:
            keep = keep + 1
        # Check if the switch has the prize
        elif player_switch == win_door:
            switch = switch + 1
print("Percentage of time if player:")
print(f"Switched: {switch/10000}")
print(f"Keep: {keep/10000}")
