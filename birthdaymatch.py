"""
Program 2 called Birthday Paradox
from Big Book of Small Python Projects
by the famous Al Sweigart

More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation
"""


import datetime, random

def getBirthdays(numberOfBirthdays):
    """Return a list of number random date objects for birthday match algorithms"""
    birthdays =[]
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def geMatch(birthdays):
    """ Return date object of any birthday that occurs more than once."""
    if len(birthdays)== let(set(birthdays)):
        return None  # all birthdays are unique in this set

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA  #
def main():
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
   
    It's not actually a paradox, it's just a surprising result.)
    47. ''')

    MONTHS = ('Jan', 'Feb',  'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec')

    while True:
        print('How many birthdays to generate? (Recommended 100 max)')
        response = input('> ')
        if response.isdecimal() and (0<int(response) <= 100):
            numBDays = int(response)
            break
    print()




    fortybirthdays = getBirthdays(40)
    print(fortybirthdays)

if __name__ == '__main__':
    main()





