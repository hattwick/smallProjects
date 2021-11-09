"""
Program 10: Cho-Han
from Big Book of Small Python Projects
by the famous Al Sweigart

Python version of Japanese dice game of even-old rolls

More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game
"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han by Al Sweigart

In this Japanese dice game, two dice are rolled in a bamboo cup by a dealer.
The player must guess if the dice total is even(Cho) or odd (Han). ''')

purse = 5000

while True:   #Main game loop
    # Place your bet:
    print("You have", purse, "mon.  How much do you bet? (or QUIT)")
    while True:
        pot = input("> ")
        if pot.upper() == 'QUIT':
            print('Thank you for playing!')
            sys.exit()


