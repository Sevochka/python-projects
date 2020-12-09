"""
    The following program is meant to be a simple coin toss guessing game. The
    player gets two guesses (it’s an easy game). However, the program has several
    bugs in it. Run through the program a few times to find the bugs that keep
    the program from working correctly
"""

import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s  -  %(message)s')

logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(f'Initial guess is {guess}')
guess = (0, 1)[guess == 'heads']
logging.debug(f'Random toss value is {toss}, while guess is {guess}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')

