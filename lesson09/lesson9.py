# Lesson 9

from random import choice

invalid = True
player = ''

while invalid:
    player = input("Enter a choice of (rock, paper, or scissors): ")
    
    if player in ('rock', 'paper', 'scissors'):
        invalid = False

cpu = choice(['rock', 'paper', 'scissors'])

if player == cpu:
    print("Tie Game")
else:
    if player == 'rock':
        if cpu == 'paper':
            print("CPU has won")
        else:
            print("The Player has won")
    elif player == 'paper':
        if cpu == 'scissors':
            print("CPU has won")
        else:
            print("The player has won")
    else:
        if cpu == 'rock':
            print("CPU has won")
        else:
            print("The player has won")