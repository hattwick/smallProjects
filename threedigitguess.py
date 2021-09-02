"""
Program 1 called Bagels
from Big Book of Small Python Projects
by the famous Al Sweigart
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels - a deductive logic game (originally by Al Sweigart).

    Guess a {}=digit number with no repeat digits.

    With each guess the system will return the following clues:
    Pico - one digit is correct but in wrong position
    Fermi - one digit is correct and in correct position
    Bagels - no digits are correct

    For example, if the secret was 248 and your guess was 843, the clue would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop
        secretNum = getSecretNum()
        print('Secret Number has been selected')
        print('the Secret Number is {}'.format(secretNum))  # TODO remove after testing
        print('You have {} guesses to solve it.'.format(MAX_GUESSES))


def getSecretNum():
    """returns a string of NUM_DIGITS unique random digits"""

    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


if __name__ == '__main__':
    main()