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

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{} '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print('You guessed it!')
                break
            if numGuesses > MAX_GUESSES:
                print("You are out of guesses")
                print("The answer was {}".format(secretNum))



def getSecretNum():
    """returns a string of NUM_DIGITS unique random digits"""

    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):

    if guess == secretNum:
        return('You got it!')

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return('Bagels - No correct numbers')

if __name__ == '__main__':
    main()
